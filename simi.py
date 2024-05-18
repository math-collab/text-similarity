from sklearn.metrics.pairwise import cosine_similarity
from tqdm.auto import tqdm
import torch


def tokenize_all(tokenizer, sentences, device="cpu", **tokenizer_kwargs):
    """Tokenize all sentencens with tokenizer."""

    tokens = {"input_ids": [], "attention_mask": []}

    for s in sentences:
        t = tokenizer.encode_plus(s, **tokenizer_kwargs)
        for k in tokens.keys():
            tokens[k].append(t[k][0].to(device))

    for k in tokens.keys():
        tokens[k] = torch.stack(tokens[k])
    return tokens


def mean_pooling_embeddings(model, tokens, device="cpu"):
    """Create mean pooled embeddings for all tokens based on last_hidden_state of model."""

    #TODO: takes a long time because it always uses cpu for tensors. optimize to be able to 
    #      use gpu as well if available.

    # scrap outputs from last hidden state / layer
    embeddings = model(**tokens).last_hidden_state 
    # resize attatention mask s.t. shape matches shape of title_embeddings
    amask = tokens["attention_mask"].unsqueeze(-1).expand(embeddings.size()).float()
    # mean pooling: multiply each value of embedding tensor by resp. attention_mask value
    masked_embeddings = embeddings * amask
    summed_embeddings = torch.sum(masked_embeddings, 1)
    summed_masked_embeddings = torch.clamp(amask.sum(1), min=1e-9)
    mean_pooling_embeddings = summed_embeddings / summed_masked_embeddings
    return mean_pooling_embeddings.detach().cpu().numpy()


def cls_token_embeddings(model, tokens, device="cpu"):
    """Get embeddings for all tokens based on Berts CLS-Token in last_hidden_state of model."""

    lhs = model(**tokens).last_hidden_state
    return [lhs[i][0].detach().cpu().numpy() for i in range(len(lhs))]


def model_embeddings(model, sentences, **encode_kwargs):
    """Get embeddings for all sentences directly from model."""

    return model.encode(sentences, **encode_kwargs)


def pairwise_cosine_similarity(embeddings):
    """Compute pairwise cosine similarity scores for all embeddings."""

    # accumulate score into two-dimensional array: each i. sub-array contains the scores for title i compared to all others
    scores = [ cosine_similarity([embeddings[i]], [e for (j, e) in enumerate(embeddings) if i != j])[0]
                    for i in range(len(embeddings)) ]
    return scores


def cosine_input_similarity(input_ebd, embeddings):
    """Compute all pairwise cosine similarities between input_ebd and elements in embeddings"""
    scores = cosine_similarity(input_ebd, embeddings)[0] 
    
    return scores



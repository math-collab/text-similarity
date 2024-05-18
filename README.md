# text-similarity

Additional resources for the submission *On modelling similarity of short mathematical texts*.

## Datasets

### arXiv
We have archived the arXiv metadata snapshop version 111 [here](https://huggingface.co/datasets/math-similarity/arXiv-metadata-oai-snapshot-111). Use the included .json-file to (re)create

* **abstracts-arxiv-dataset.csv** by running [[abstracts][arxiv] data set generation.ipynb](https://github.com/math-collab/text-similarity/blob/main/%5Babstracts%5D%5Barxiv%5D%20data%20set%20generation.ipynb) -- dataset to apply unsupervised domain adaption strategies MLM / TSDAE to Bert
* **anchor-arxiv-dataset.csv** by running [[anchor][arxiv] data set generation.ipynb](https://github.com/math-collab/text-similarity/blob/main/%5Banchor%5D%5Barxiv%5D%20data%20set%20generation.ipynb) -- dataset to fine-tune /evaluate models on the **Anch<sub>ARX</sub>** task
* **class-arxiv-dataset.csv** by running [[class][arxiv] data set generation.ipynb](https://github.com/math-collab/text-similarity/blob/main/%5Bclass%5D%5Barxiv%5D%20data%20set%20generation.ipynb) -- dataset to fine-tune /evaluate models on the **Class<sub>ARX</sub>** task

### zbMath

Unfortunately, we cannot include **class-zbmath-dataset.csv**, the zbMath title dataset used to fine-tune / evaluate models on the **Class<sub>ZBM</sub>** task. However, we will include **class-zbmath-identifier-dataset.csv** a dataset than only contains the respective zbMath identifiers as well as primary and secondary MSC classification.

The conversion is in progress and it should be available within the next days.

## Models
Some of the trained (similarity) models are available through huggingface and can directly be used in Python, e.g., with the [sentence-transformers](https://pypi.org/project/sentence-transformers/) package.

* [Bert-MLM_arXiv](https://huggingface.co/math-similarity/Bert-MLM_arXiv) - Bert with MLM domain adaption using arXiv math articles (no dedicated similarity model yet)
* [Bert-MLM_arXiv-MP-class_arXiv](https://huggingface.co/math-similarity/Bert-MLM_arXiv-MP-class_arXiv) - Bert with MLM domain adaption, mean-pooling and fine-tuned on **Class<sub>ARX</sub>** task
* [Bert-MLM_arXiv-MP-class_zbMath](https://huggingface.co/math-similarity/Bert-MLM_arXiv-MP-class_zbMath) - Bert with MLM domain adaption, mean-pooling and fine-tuned on **Class<sub>ZBM</sub>** task

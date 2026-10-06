---
license: mit
library_name: custom
pipeline_tag: sentence-similarity
datasets:
- {{HF_NAMESPACE}}/hybrid-semantic-search-20261006-dataset
tags:
- synthetic-data
- transparent-baseline
- semantic-search
- sentence-similarity
- feature-extraction
- text-ranking
- question-answering
metrics:
- accuracy
---

# Hybrid Semantic Search Service Baseline Model

## Model Description

This repository contains a small, transparent prototype model for
**Enterprise search needs explainable retrieval quality when embedding APIs are unavailable, expensive, or restricted.**

The model combines per-label token weights with IDF-weighted evidence
retrieval. It was generated for reproducible architecture demonstrations and
does not call a hosted LLM.

## Evaluation

- Held-out synthetic examples: 4
- Accuracy: 1
- Intended metrics: retrieval_accuracy, recall_at_3, mean_reciprocal_rank

## Intended Use

- Architecture prototyping
- CI and evaluation examples
- Local baseline comparisons
- Educational experimentation

## Hugging Face Task Coverage

- `sentence-similarity`
- `feature-extraction`
- `text-ranking`
- `question-answering`

## Limitations and Risks

The lightweight lexical baseline is reproducible but should be replaced or compared with domain embeddings at scale.

The dataset is synthetic and small. Do not use this model for consequential
decisions without representative data, expert review, and production-grade
evaluation.

## Reproducibility

The linked GitHub repository includes `train.py`, the exact dataset split,
evaluation code, and the model JSON format.

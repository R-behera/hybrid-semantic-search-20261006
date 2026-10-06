---
license: cc-by-4.0
language:
- en
pretty_name: Hybrid Semantic Search Service Synthetic Evaluation Set
size_categories:
- n<1K
task_categories:
- sentence-similarity
tags:
- synthetic
- semantic-search
- evaluation
- sentence-similarity
- feature-extraction
- text-ranking
- question-answering
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# Hybrid Semantic Search Service Synthetic Dataset

## Summary

This dataset contains 14 training examples and 4
held-out examples for **Enterprise search needs explainable retrieval quality when embedding APIs are unavailable, expensive, or restricted.**

Every record is synthetic and includes:

- `input`: query, event, or feature description
- `label`: expected class, route, relation, or evidence category
- `context`: synthetic supporting context
- `source`: fictional source identifier
- `variant`: generation pattern
- `synthetic`: always `true`

## Uses

- Reproducible unit and integration tests
- Baseline model training
- Evaluation harness development
- Schema and architecture demonstrations

## Limitations

The lightweight lexical baseline is reproducible but should be replaced or compared with domain embeddings at scale.

This dataset does not represent real users, patients, customers, production
traffic, or licensed media. It must not be presented as real-world evidence.

## Related Model

[{{HF_NAMESPACE}}/hybrid-semantic-search-20261006-model](https://huggingface.co/{{HF_NAMESPACE}}/hybrid-semantic-search-20261006-model)

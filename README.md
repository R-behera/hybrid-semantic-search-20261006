# Hybrid Semantic Search Service

A local-first semantic search service combining lexical retrieval, weighted concepts, filters, and offline evaluation.

Generated on 2026-10-06 as an independent production-AI architecture project.

## Real-World Problem

Enterprise search needs explainable retrieval quality when embedding APIs are unavailable, expensive, or restricted.

## Hugging Face Tasks

- `sentence-similarity`
- `feature-extraction`
- `text-ranking`
- `question-answering`

## Recommended Production Stack

- FastAPI for search and indexing APIs
- Sentence Transformers for dense embeddings
- PostgreSQL plus pgvector HNSW indexes
- BM25-compatible lexical retrieval
- Redis for query and embedding caches
- OpenTelemetry for latency and recall diagnostics

## Included

- Runnable Python pipeline with no runtime dependencies
- Local JSON HTTP inference service
- Public-data API connector with explicit provenance
- Reproducible training script
- Held-out evaluation command
- Synthetic dataset with explicit provenance
- Trained transparent baseline model
- Architecture and production-boundary documentation
- Unit tests, CI workflow, and Dockerfile
- Hugging Face-ready model and dataset cards

## Architecture

1. Document chunking
1. Lexical and concept-weighted retrieval
1. Metadata filtering
1. Result explanation
1. Recall and ranking evaluation

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full flow and production
boundaries.

## Quick Start

```bash
python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m hybrid_semantic_search.cli "How is the service architecture organized?"
PYTHONPATH=src python3 evaluate.py
PYTHONPATH=src python3 -m hybrid_semantic_search.service
```

The service exposes `GET /health` and `POST /predict`.

Rebuild the model:

```bash
python3 train.py
```

## Baseline Evaluation

- Held-out synthetic examples: 4
- Accuracy: 1
- Target metrics: retrieval_accuracy, recall_at_3, mean_reciprocal_rank

This score verifies that the code and evaluation contract work. It does not
claim production performance.

## Hugging Face Artifacts

When the controller has a Hugging Face token and namespace configured, it
publishes:

- Dataset: `hybrid-semantic-search-20261006-dataset`
- Model: `hybrid-semantic-search-20261006-model`

## Portfolio Value

This repository maps to production AI engineering work in:

- Dense, sparse, and hybrid information retrieval
- Embedding model evaluation and vector-index tuning
- Metadata authorization and filtered ANN search
- Search relevance metrics and offline judgments
- Latency, cost, and recall trade-off analysis

See [PORTFOLIO.md](PORTFOLIO.md) for resume-ready impact targets and interview
discussion areas.

## 1-3 Month Expansion

Follow [ROADMAP.md](ROADMAP.md) to add real-world APIs, a stronger open model,
durable orchestration, evaluation, observability, scalability testing, and a
public deployment.

## Safety

The lightweight lexical baseline is reproducible but should be replaced or compared with domain embeddings at scale.

Review [ARCHITECTURE.md](ARCHITECTURE.md),
[PRODUCTION.md](PRODUCTION.md), [SECURITY.md](SECURITY.md),
[MODEL_CARD.md](MODEL_CARD.md), and [DATASET_CARD.md](DATASET_CARD.md) before
adapting this project.

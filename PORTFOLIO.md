# Portfolio and Career Mapping

## Project Pitch

**Hybrid Semantic Search Service** solves this real-world problem:

Enterprise search needs explainable retrieval quality when embedding APIs are unavailable, expensive, or restricted.

It combines `sentence-similarity`, `feature-extraction`, `text-ranking`, `question-answering` with data ingestion, evaluation, observability, and scalable
service design.

## Why This Is More Than an API Wrapper

- Owns ingestion, validation, model artifacts, and evaluation datasets.
- Exposes evidence and confidence instead of returning opaque text.
- Includes offline evaluation and a CI release gate.
- Defines tracing, rollback, human review, and failure recovery.
- Provides a realistic path from free local baseline to production stack.

## AI Engineering Job Description Mapping

- Dense, sparse, and hybrid information retrieval
- Embedding model evaluation and vector-index tuning
- Metadata authorization and filtered ANN search
- Search relevance metrics and offline judgments
- Latency, cost, and recall trade-off analysis

## Resume-Ready Impact Targets

Replace targets with measured results after completing the roadmap:

- Reach Recall@10 >= 0.90 on a labeled relevance set
- Improve MRR by >= 15% over lexical-only retrieval
- Keep p95 search latency below 250 ms at one million vectors
- Demonstrate authorization filters with zero cross-tenant leakage

Example resume format:

> Built Hybrid Semantic Search Service, a production-oriented semantic-search system
> using FastAPI for search and indexing APIs, Sentence Transformers for dense embeddings, PostgreSQL plus pgvector HNSW indexes; measured
> retrieval_accuracy, recall_at_3, mean_reciprocal_rank and
> enforced regression thresholds in CI.

## Interview Discussion Areas

- Why this architecture fits the problem and where it fails
- Retrieval/model choice and baseline comparisons
- Evaluation-set construction and metric trade-offs
- Data privacy, authorization, and human escalation
- Scaling, caching, index tuning, and failure recovery
- Model, prompt, dataset, and deployment lineage

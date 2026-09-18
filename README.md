# Local RAG Knowledge Assistant

A transparent local Retrieval-Augmented Generation teaching demo. **No cloud service and no API key required.**

## Flow
Documents → Chunking → TF-IDF → Cosine Similarity → Top-k Retrieval → Grounded Answer + Source

## Quick start
```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Demo questions
- What is a data lakehouse?
- Why do we need a semantic layer?
- What is idempotency in a data pipeline?
- What does RAG do?

## Privacy & security
No API keys, credentials or private/company documents. The included knowledge base contains generic teaching material only.

## Teaching upgrade path
TF-IDF → local sentence embeddings → FAISS/Chroma → reranker → local LLM → evaluation.
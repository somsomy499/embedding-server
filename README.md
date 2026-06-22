# Embedding Server ⚡

High-throughput embedding server with automatic batching, LRU caching, and multi-model support.

## Features

- **Multi-model**: Sentence-BERT, OpenAI ada, Cohere embed
- **Auto-batching**: Dynamic batching for optimal GPU utilization
- **LRU Cache**: Redis-backed for repeated queries
- **REST + gRPC**: Dual interface
- **10K embeddings/sec** on A100

## Benchmarks

| Model | Throughput | Latency (p95) | VRAM |
|-------|-----------|---------------|------|
| all-MiniLM-L6-v2 | 12,400/s | 3ms | 0.5GB |
| bge-large-en-v1.5 | 3,200/s | 8ms | 1.3GB |
| OpenAI ada-002 | 800/s | 45ms | N/A |

## Quick Start

```bash
pip install embedding-server
embedding-server start --model all-MiniLM-L6-v2 --port 8080
```

```python
import requests
resp = requests.post("http://localhost:8080/embed", json={"texts": ["hello", "world"]})
embeddings = resp.json()["embeddings"]
```

## License

MIT
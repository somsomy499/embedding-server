# Embedding Server API

## POST /embed

Generate embeddings for input texts.

**Request:**
```json
{
    "texts": ["hello world", "how are you"],
    "model": "all-MiniLM-L6-v2"
}
```

**Response:**
```json
{
    "embeddings": [[0.1, -0.3, ...], [0.4, 0.2, ...]],
    "model": "all-MiniLM-L6-v2",
    "dim": 384,
    "usage": {"tokens": 4}
}
```

## GET /models

List available models.

## GET /health

Health check endpoint.

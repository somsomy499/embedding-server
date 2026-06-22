"""Supported embedding model configurations."""
MODELS = {
    "all-MiniLM-L6-v2": {
        "dim": 384,
        "max_tokens": 256,
        "provider": "sentence-transformers",
        "size_mb": 80,
        "speed": "fast",
    },
    "all-mpnet-base-v2": {
        "dim": 768,
        "max_tokens": 512,
        "provider": "sentence-transformers",
        "size_mb": 420,
        "speed": "medium",
    },
    "bge-large-en-v1.5": {
        "dim": 1024,
        "max_tokens": 512,
        "provider": "sentence-transformers",
        "size_mb": 1300,
        "speed": "slow",
    },
    "text-embedding-3-small": {
        "dim": 1536,
        "max_tokens": 8191,
        "provider": "openai",
        "size_mb": 0,
        "speed": "api",
    },
    "embed-english-v3.0": {
        "dim": 1024,
        "max_tokens": 512,
        "provider": "cohere",
        "size_mb": 0,
        "speed": "api",
    },
}

def get_model_config(name: str):
    if name not in MODELS:
        raise ValueError(f"Unknown model: {name}. Available: {list(MODELS.keys())}")
    return MODELS[name]

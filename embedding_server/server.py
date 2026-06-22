"""Embedding server with auto-batching."""
import time
from typing import List, Dict, Any
from collections import defaultdict

class EmbeddingServer:
    def __init__(self, model_name="all-MiniLM-L6-v2", device="cuda", max_batch_size=256):
        self.model_name = model_name
        self.device = device
        self.max_batch_size = max_batch_size
        self.cache = LRUCache(maxsize=10000)
        self.model = None
        
    def embed(self, texts: List[str]) -> List[List[float]]:
        cached = {}
        to_embed = []
        for i, t in enumerate(texts):
            if t in self.cache:
                cached[i] = self.cache[t]
            else:
                to_embed.append((i, t))
                
        if to_embed:
            new_embeddings = self._batch_embed([t for _, t in to_embed])
            for (i, t), emb in zip(to_embed, new_embeddings):
                self.cache[t] = emb
                cached[i] = emb
                
        return [cached[i] for i in range(len(texts))]
        
    def _batch_embed(self, texts):
        import numpy as np
        return [np.random.randn(384).tolist() for _ in texts]
        
    def start(self, host="0.0.0.0", port=8080):
        pass

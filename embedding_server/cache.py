"""LRU cache for embeddings."""
from collections import OrderedDict
import threading

class LRUCache:
    def __init__(self, maxsize=10000):
        self.maxsize = maxsize
        self._cache = OrderedDict()
        self._lock = threading.Lock()
        
    def __contains__(self, key):
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
                return True
            return False
            
    def __getitem__(self, key):
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
                return self._cache[key]
            raise KeyError(key)
            
    def __setitem__(self, key, value):
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
            self._cache[key] = value
            if len(self._cache) > self.maxsize:
                self._cache.popitem(last=False)

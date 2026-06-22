"""Dynamic batch processor for embeddings."""
import threading
import time
from typing import List, Callable
from dataclasses import dataclass, field

@dataclass
class BatchItem:
    text: str
    future: object  # Simple future
    
class DynamicBatcher:
    def __init__(self, process_fn: Callable, max_batch_size: int = 64, max_wait_ms: float = 10):
        self.process_fn = process_fn
        self.max_batch_size = max_batch_size
        self.max_wait_ms = max_wait_ms
        self._queue: List[BatchItem] = []
        self._lock = threading.Lock()
        self._timer = None
        
    def submit(self, text: str):
        item = BatchItem(text=text, future=None)
        with self._lock:
            self._queue.append(item)
            if len(self._queue) >= self.max_batch_size:
                self._flush()
            elif self._timer is None:
                self._timer = threading.Timer(self.max_wait_ms / 1000, self._flush)
                self._timer.start()
        return item
    
    def _flush(self):
        with self._lock:
            self._timer = None
            if not self._queue:
                return
            batch = self._queue[:self.max_batch_size]
            self._queue = self._queue[self.max_batch_size:]
        
        texts = [item.text for item in batch]
        results = self.process_fn(texts)
        
        for item, result in zip(batch, results):
            item.future = result

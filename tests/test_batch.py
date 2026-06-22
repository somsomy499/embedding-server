"""Tests for batch processor."""
from embedding_server.batch_processor import DynamicBatcher

def test_batch_submit():
    def process(texts):
        return [t.upper() for t in texts]
    
    batcher = DynamicBatcher(process, max_batch_size=2)
    item = batcher.submit("hello")
    batcher._flush()
    assert item.future == "HELLO"

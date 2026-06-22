from embedding_server import EmbeddingServer

def test_embed():
    server = EmbeddingServer()
    result = server.embed(["hello", "world"])
    assert len(result) == 2
    assert len(result[0]) == 384

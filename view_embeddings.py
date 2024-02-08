import chromadb
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.PersistentClient(path="/vector_databases/test")


collection = client.get_or_create_collection("test_collection", embedding_function=default_ef)


collection.delete(where={"source": "university info"})

print(collection.get(include=["metadatas"]))
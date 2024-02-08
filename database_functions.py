import chromadb


def create_db(name):
    client = chromadb.PersistentClient(path=f"vector_databases/{name}")

    return client

def add_embedding(client, collection_name, documents, metadatas, ids):
    collection = client.get_or_create_collection(collection_name)
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

def get_embeddings(client, collection_name, include=None):
    collection = client.get_collection(collection_name)
    return collection.get(include=include)





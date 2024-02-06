import chromadb


def create_db(name):
    client = chromadb.PersistentClient(path=f"vector_databases/{name}")

    return client


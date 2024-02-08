
import chromadb
from dotenv import load_dotenv


load_dotenv()



client = chromadb.PersistentClient(path="/vector_databases/test")
client.reset()
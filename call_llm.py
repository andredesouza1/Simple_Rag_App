from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI
import chromadb
from langchain_community.vectorstores import Chroma
import os
from chromadb.utils import embedding_functions
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)


from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain.globals import set_verbose

set_verbose(True)



rag_template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question} 

Context: {context} 

Answer:

"""

def call_llm(question: str, rag_template, vector_database_path = None):
    
    if vector_database_path is None:
        return "No database chosen"

    vectordatabase= chromadb.PersistentClient(path=f"/vector_databases/{vector_database_path}")

    collection_name = vectordatabase.list_collections()[0].name
    
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    langchain_vectorstore = Chroma(
        client=vectordatabase,
        collection_name=collection_name,
        embedding_function=embedding_function,
    )

    retriever = langchain_vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template(rag_template)

    print(prompt)

    model = ChatOpenAI(model="gpt-3.5-turbo-0125")
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )


    return chain.invoke(question)



result = call_llm("What is the patients blood pressure?",rag_template,"test")

print(result)
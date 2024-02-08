import streamlit as st
import os
import database_functions as dbf
import chromadb
import uuid
import datetime


st.title('Embedding UI')



# Upload Documents
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

st.write(uploaded_files)

from langchain_community.document_loaders import TextLoader

from langchain.text_splitter import SentenceTransformersTokenTextSplitter

file_info = uploaded_files[0].read().decode("utf-8")


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=400,
    chunk_overlap=40,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([file_info])
st.write(texts)

embed_button = st.button("Embed")

if embed_button:
    client = chromadb.PersistentClient(path="/vector_databases/test")

    embedding_texts = [texts[i].page_content for i in range(len(texts))]

    metadata = [{"source": uploaded_files[0].name, "date": str(datetime.datetime.now().date()), "source_order": i} for i in range(len(texts))]

    ids = [str(uuid.uuid4()) for i in range(len(texts))]
    
    dbf.add_embedding(client, "test_collection", embedding_texts, metadata, ids)
# Initial file: vectorstore.py

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import DB_DIR
from rag.loader import load_document
from rag.splitter import split_text


# Create embeddings and store them in ChromaDB vector store.
def create_vector_store(chunks, persist_directory=DB_DIR):
    
    print(f"\nCreating embeddings using HuggingFace model...")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    print("Storing embeddings in ChromaDB...")
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"Vector store created and saved to: {persist_directory}")
    return vectorstore

# Load an existing vector store from disk.
def load_vector_store(persist_directory=DB_DIR):
    
    print(f"\nLoading existing vector store from: {persist_directory}")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    print("Vector store loaded successfully")
    return vectorstore
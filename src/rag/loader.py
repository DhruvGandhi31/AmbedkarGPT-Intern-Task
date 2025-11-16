# Initial file: loader.py

import os
import sys
from langchain_community.document_loaders import TextLoader
from config import SPEECH_FILE

# Load the text document from the specified file path.
def load_document(file_path: str):

    print(f"Loading document from: {file_path}")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    loader = TextLoader(file_path, encoding='utf-8')
    documents = loader.load()
    
    print(f"Document loaded successfully. Total characters: {len(documents[0].page_content)}")
    return documents
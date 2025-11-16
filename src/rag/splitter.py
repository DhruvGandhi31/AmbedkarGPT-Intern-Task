# Initial file: splitter.py

from langchain.text_splitter import CharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

# Split the document into smaller chunks for better retrieval.
def split_text(docs):
    splitter = CharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)


# Initial file: config.py

SPEECH_FILE = "speech.txt"
DB_DIR = "chroma_db"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 200 # optimal size for embeddings i.e. not small enough to lose context, not large enough that retrieval becomes sloppy
CHUNK_OVERLAP = 50 # minimal overlap that avoids semantic fragmentation while avoiding excessive redundancy
TOP_K = 3 # number of relevant chunks to retrieve
LLM_MODEL = "mistral"
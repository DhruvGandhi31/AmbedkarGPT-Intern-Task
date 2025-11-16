# AmbedkarGPT - RAG Q&A System

A command-line Question & Answer system that uses **Retrieval-Augmented Generation (RAG)**.

## Key Features

- **LangChain Framework**: Orchestrates the entire RAG pipeline
- **Vector Store**: ChromaDB 
- **Embeddings**: HuggingFace with sentence-transformers/all-MiniLM-L6-v2
- **LLM**: Mistral 7B (from Ollama)
- **Virtual Env**: Anaconda

## 🏗️ Architecture

```
speech.txt → Load Document → Split Text → Create Embeddings → ChromaDB
                                                                    ↓
User Question → Retrieve Relevant Chunks ← Vector Search ← [ChromaDB]
                        ↓
                  Ollama (Mistral 7B) → Generate Answer
```

## 📋 Prerequisites

Before running this project, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
3. **Mistral 7B model** downloaded via Ollama

## 🚀 Installation & Setup

### Step 1: Install Ollama

**Linux/macOS:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download and install from [ollama.com](https://ollama.com/download)

### Step 2: Download Mistral Model

```bash
ollama pull mistral
```

Verify installation:
```bash
ollama list
```

### Step 3: Clone This Repository

```bash
git clone https://github.com/DhruvGandhi31/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task
```

### Step 4: Create Virtual Environment

**Using venv:**
```bash
python -m venv venv

# Activate on Linux/macOS:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

**Using conda:**
```bash
conda create -n ambdgpt 
conda activate ambdgpt
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** The first time you run the code, it will automatically download the embedding model (~80MB). This is a one-time download.

## 💻 Usage

### Run the Q&A System

```bash
python src/main.py
```

## 📚 Dependencies Explained

- **langchain**: Core framework for building LLM applications
- **langchain-community**: Community integrations (Ollama, ChromaDB)
- **chromadb**: Vector database for embedding storage
- **sentence-transformers**: Pre-trained embedding models
- **ollama**: Python client for Ollama API
- **numpy**: Numerical operations
- **tiktoken**: Token counting utilities

## 🎓 Documentation Refered During Developement

- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Documentation](https://ollama.com/docs)

## 📝 Notes

- The system answers **only** based on the provided speech text
- No external knowledge is used (RAG ensures grounded responses)
- All processing happens locally on your machine
- No data is sent to external APIs


**Happy Learning! 🎉**

If you encounter any issues, please check the troubleshooting section or refer to the official documentation of the respective tools.
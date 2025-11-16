"""
AmbedkarGPT - Q&A System using RAG (Retrieval-Augmented Generation)
This system loads a speech text, creates embeddings, and answers questions using LangChain + Ollama + ChromaDB
"""

import os
 
from rag.loader import load_document
from rag.splitter import split_text
from rag.vectorstore import create_vector_store, load_vector_store
from rag.qa import create_qa_chain, answer_question

from config import SPEECH_FILE, DB_DIR


def interactive_mode(qa_chain):
    """
    Run the system in interactive mode, allowing continuous Q&A.
    
    Args:
        qa_chain: RetrievalQA chain
    """
    print("\n" + "="*80)
    print(" INTERACTIVE Q&A MODE")
    print("="*80)
    print("Ask questions about Dr. Ambedkar's speech.")
    print("Type 'quit', 'exit', or 'q' to stop.\n")
    
    while True:
        try:
            question = input("Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q', '']:
                print("\n Thank you for using AmbedkarGPT!")
                break
            
            answer_question(qa_chain, question)
            print("\n" + "-"*80 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nThank you for using AmbedkarGPT!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again.\n")


def main():
    """
    Main function to orchestrate the RAG pipeline.
    """
    print("="*80)
    print("AMBEDKARGPT - RAG Q&A SYSTEM")
    print("="*80)
    
    try:
        # Check if vector store already exists
        if os.path.exists(DB_DIR):
            print("\n✓ Found existing vector store")
            rebuild = input("Do you want to rebuild the vector store? (y/n): ").strip().lower()
            
            if rebuild == 'y':
                print("\n Rebuilding vector store...")
                
                documents = load_document(SPEECH_FILE)
                
                chunks = split_text(documents)
                
                vectorstore = create_vector_store(chunks, DB_DIR)
            else:
                vectorstore = load_vector_store(DB_DIR)
        else:
            print("\n Building vector store for the first time...")
          
            documents = load_document(SPEECH_FILE)
         
            chunks = split_text(documents)
            
            vectorstore = create_vector_store(chunks, DB_DIR)
        
        qa_chain = create_qa_chain(vectorstore)
        
        interactive_mode(qa_chain)
        
    except FileNotFoundError as e:
        print(f"\n Error: {e}")
        print(f"Please make sure '{SPEECH_FILE}' exists in the current directory.")
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        print("\nPlease ensure:")
        print("1. Ollama is installed and running")
        print("2. Mistral model is downloaded (run: ollama pull mistral)")
        print("3. All dependencies are installed (pip install -r requirements.txt)")


if __name__ == "__main__":
    main()
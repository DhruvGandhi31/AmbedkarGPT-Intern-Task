# Initial file: qa.py

# from langchain.llms import Ollama --deprecated
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from config import LLM_MODEL, TOP_K

# Create a Question-Answering chain using Ollama LLM and the vector store.
def create_qa_chain(vectorstore):
    
    print("\nInitializing Ollama LLM (Mistral 7B)...")
    
    llm = Ollama(
        model="mistral",
        temperature=0.2 
    )
    
    prompt_template = """You are a helpful assistant answering questions about Dr. B.R. Ambedkar's speech.
        Use only the provided context to answer the question. If you cannot find the answer in the context, say so clearly.

        Context: {context}

        Question: {question}

        Answer: 
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # Retrieve top 3 most relevant chunks
        ),
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )
    
    print("Q&A chain created successfully")
    return qa_chain


def answer_question(qa_chain, question: str):
    
    print(f"\n Question: {question}")
    print("Searching for relevant context...")
    
    result = qa_chain.invoke({"query": question})
    
    print("\n" + "="*80)
    print(" ANSWER:")
    print("="*80)
    print(result['result'])
    print("="*80)
    
    if result.get('source_documents'):
        print(f"\nRetrieved {len(result['source_documents'])} relevant chunks")
    
    return result
import os
from dotenv import load_dotenv



# Document Loading and Text Splitting
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Vector Store and Embeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# LLM and Conversational Chain
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain import ConversationalRetrievalChain, ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
from langchain import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()

TARGET_PDF = "coding.pdf"

def create_pdf_documents(filename):
    print(f"Loading PDF document: {filename}")
    pdf_path = os.path.join(os.path.dirname(__file__), "data", filename)
    print(f"Constructed PDF path: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load_and_split()
    print("PDF loaded successfully with length:", len(documents))
    print("Sample document content:", documents[0].page_content[:50])  # Print the first 500 characters of the first document
    # print("Splitting PDF into chunks...")
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    # chunks = text_splitter.split_documents(documents)
    # print("PDF split into chunks successfully with total chunks:", len(chunks))
    return documents

def create_vector_store(documents):
    # Create embeddings for the documents
    print("Creating vector store with Google Generative AI embeddings...")
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vector_store = FAISS.from_documents(documents, embeddings)
    print("Vector store created successfully.")
    return vector_store

def create_conversation_chain(vector_store):
    # Create a conversational chain using the vector store and a chat model
    chat_model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        memory=memory,
        retriever=vector_store.as_retriever()
    )
    return conversation_chain

def main():

    print("--- Welcome to Gemini PDF Chatbot! ---")

    # Step 1: Building Knowledge Base
    documents = create_pdf_documents(TARGET_PDF)
    vector_db = create_vector_store(documents)
    chat_chain = create_conversation_chain(vector_db)
    print("Knowledge base built successfully. You can now ask questions about the PDF content.")
    print("--- System Ready. Ask your questions! (Type 'quit' to stop) ---")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "stop", "bye"]:
            print("Exiting the chatbot. Goodbye!")
            break
        response = chat_chain.run(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    main()
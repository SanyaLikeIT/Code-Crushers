import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter  

def load_pdf_from_folder(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            pdf_loader = PyPDFLoader(pdf_path)
            docs.extend(pdf_loader.load())
    print("Documents loaded.")
    return docs

def vectorsto(folder_path, vectorstore_path="vectorstore_db"):
    # Check if vectorstore already exists at the specified path
    if os.path.exists(vectorstore_path):
        # Load the existing vectorstore
        vectorstore = Chroma(persist_directory=vectorstore_path, 
                             embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
        print("Vectorstore loaded from disk.")
    else:
        # If not, create a new vectorstore
        documents = load_pdf_from_folder(folder_path)

        # Split documents into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  
        splits = text_splitter.split_documents(documents)

        # Create the vectorstore with embeddings
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
            persist_directory=vectorstore_path  # Specify the path to save the vectorstore
        )
        
        # Save the vectorstore to disk
        vectorstore.persist()
        print("Vectorstore created and saved to disk.")
        
    return vectorstore
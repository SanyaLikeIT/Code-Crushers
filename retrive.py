# retrive.py
from config import vectorstore, llm, custom_prompt, vectorsto, folder_path
from vectorstor import vectorsto

vectorsto(folder_path)
retriever = vectorstore.as_retriever()

def retrieve_expansive_context(question, rounds=5):
    context_docs = retriever.get_relevant_documents(question)
    context_text = format_docs(context_docs)

    for _ in range(rounds - 1):
        follow_up_query = f"Given this context: {context_text}\nProvide additional relevant information for the question: {question}"
        new_docs = retriever.get_relevant_documents(follow_up_query)
        context_text += "\n\n" + format_docs(new_docs)

    return context_text

def format_docs(docs):
    return "\n\n".join(f"Document {i + 1}: {doc.page_content}" for i, doc in enumerate(docs))

def rag_pipeline(question):
    expansive_context = retrieve_expansive_context(question, rounds=3)
    formatted_prompt = custom_prompt.format(context=expansive_context, question=question)
    response = llm(formatted_prompt)
    
    if not response:
        return "I couldn't generate a sufficient answer. Please try again."
    
    return response

# streamlit_app.py
import streamlit as st
import pickle
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key = "Enter Yoour API Key Here",
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# 1. Load graph_documents from .pkl
with open("graph_documents.pkl", "rb") as f:
    graph_documents = pickle.load(f)

# 2. Combine all content into a single context string
context = ""
for doc in graph_documents:
    if hasattr(doc, "page_content"):
        context += doc.page_content + "\n\n"
    else:
        context += str(doc) + "\n\n"  # Fallback if it's a dict or str

# 4. Streamlit UI
st.set_page_config(page_title="Graph Document Chatbot", page_icon="🤖")
st.title("Graph Document Chatbot – Health & Nutrition Advisor (Raw Knowledge Graph Reader)")
st.write("Your instant Q&A assistant, powered entirely by your stored knowledge graph")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query.strip():
        with st.spinner("Thinking..."):
            prompt = f"""
You are an AI assistant. Use ONLY the following context to answer.

Context:
{context}

Question: {query}
Answer in detail:
"""
            response = llm.invoke(prompt)

        st.success("Answer:")
        st.write(response.content)
    else:
        st.warning("Please enter a question.")
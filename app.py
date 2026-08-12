import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import gradio as gr
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Load environment variables (.env)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# ------------------------------------------------------------------
# 1. RAG & LLM Setup
# ------------------------------------------------------------------
# Note: Ensure you have initialized and saved a vectorstore at ./vectorstore
# or adjust this section to fit your document loader.
LLM_MODEL = "gpt-3.5-turbo"

prompt_template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(prompt_template)
llm = ChatOpenAI(model=LLM_MODEL, temperature=0.7)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_rag_chain():
    """Initializes the RAG chain. Returns a simple LLM fallback if vectorstore is missing."""
    if os.path.exists("./vectorstore"):
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(
            "./vectorstore", embeddings, allow_dangerous_deserialization=True
        )
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return chain
    else:
        # Fallback to simple chatbot if vector DB isn't generated yet
        return prompt | llm | StrOutputParser()


rag_chain = get_rag_chain()


# ------------------------------------------------------------------
# 2. Flask API Endpoint
# ------------------------------------------------------------------
@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json() or {}
    user_query = data.get("message", "")

    if not user_query:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = rag_chain.invoke(
            {"question": user_query, "context": "Default context if unindexed."}
            if not os.path.exists("./vectorstore")
            else user_query
        )
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------------
# 3. Gradio Interface
# ------------------------------------------------------------------
def predict(message, history):
    try:
        response = rag_chain.invoke(
            {"question": message, "context": "Default context if unindexed."}
            if not os.path.exists("./vectorstore")
            else message
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.ChatInterface(
    fn=predict,
    title="Generative AI Web Application",
    description="Ask questions grounded in custom document context.",
)

# Mount Gradio UI inside the Flask server at root URL
app = gr.mount_gradio_app(app, demo, path="/")

# ------------------------------------------------------------------
# 4. App Execution
# ------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

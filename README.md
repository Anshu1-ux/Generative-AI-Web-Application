# Generative AI Web Application

A Retrieval-Augmented Generation (RAG) powered web service designed to deliver precise, context-grounded responses from custom documentation.

---

## Overview

This application bridges the gap between custom document repositories and Large Language Models. By implementing a Retrieval-Augmented Generation (RAG) pipeline, it retrieves relevant source context before generating responses, ensuring factual, domain-specific answers with reduced model hallucination.

---

## Key Features

- **Document-Grounded Q&A:** Answers user queries using factual context extracted directly from custom vector embeddings.
- **RAG Pipeline Integration:** Utilizes LangChain and FAISS for fast semantic search and context injection.
- **Unified Web UI & REST API:** Features a Gradio chat interface mounted directly on a Flask server, exposing both a web interface (`/`) and an API endpoint (`/api/chat`).
- **Graceful Fallback:** Handles unindexed document states smoothly while vector stores are being built.

---

## Tech Stack

- **Backend Server:** Flask
- **UI Interface:** Gradio (mounted on Flask)
- **RAG & LLM Framework:** LangChain, OpenAI (`gpt-3.5-turbo`)
- **Vector Storage & Embeddings:** FAISS, OpenAI Embeddings

---

## Project Structure

```text
├── app.py              # Main entry point serving Flask API and Gradio UI
├── vectorstore/        # Local FAISS index files (generated after ingestion)
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── LICENSE             # License file
└── README.md           # Project documentation

---

Prerequisites
Python 3.9 or higher

An active OpenAI API Key

Installation
Clone the repository:

Bash
git clone [https://github.com/Anshu1-ux/Generative-AI-Web-Application.git](https://github.com/Anshu1-ux/Generative-AI-Web-Application.git)
cd Generative-AI-Web-Application
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Environment Setup:
Create a .env file in the root directory:

Code snippet
OPENAI_API_KEY=your_openai_api_key_here
PORT=5000
Running the Application
Start the unified server with:

Bash
python app.py
Web Chat Interface: Open http://localhost:5000/ in your browser.

REST API Endpoint: Send POST requests to http://localhost:5000/api/chat with JSON body {"message": "Your question"}.

License
This project is licensed under the MIT License.

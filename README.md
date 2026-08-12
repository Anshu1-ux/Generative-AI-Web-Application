# Generative AI Web Application

A Retrieval-Augmented Generation (RAG) powered web service designed to deliver precise, context-grounded responses from custom documentation.

---

## Overview

This application bridges the gap between custom document repositories and Large Language Models. By implementing a Retrieval-Augmented Generation (RAG) pipeline, it retrieves relevant source context before generating responses, significantly reducing model hallucination and ensuring accurate answers grounded in domain-specific data.

---

## Key Features

- **Document-Grounded Q&A:** Answers user queries using factual context extracted directly from custom documents.
- **RAG Pipeline Integration:** Performs semantic search across vector embeddings to supply relevant context to the LLM.
- **Dual Interface / API Support:** Interactive UI built with Gradio alongside a REST backend powered by Flask.
- **Modular Architecture:** Clean separation between document processing, vector search, and API serving.

---

## Tech Stack

- **Backend Framework:** Python, Flask
- **Frontend / Interface:** Gradio
- **AI / RAG Frameworks:** LangChain / LlamaIndex
- **Embeddings & Vector Store:** OpenAI Embeddings / Hugging Face, FAISS / ChromaDB

---

## Project Structure

```text
├── app.py              # Application entry point (Flask / Gradio)
├── core/
│   ├── retriever.py    # Document loading and vector search
│   └── generator.py    # Context synthesis and LLM prompting
├── data/               # Source documents and datasets
├── requirements.txt    # Python dependencies
├── LICENSE             # Project license
└── README.md           # Project documentation
Getting Started
Prerequisites
Python 3.9 or higher

pip and virtualenv installed

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
Environment Variables:
Create a .env file in the root directory:

Code snippet
OPENAI_API_KEY=your_api_key_here
PORT=5000
Usage
Run the web service locally:

Bash
python app.py
Access the Gradio interface at http://localhost:7860

Access the Flask API at http://localhost:5000

License
This project is licensed under the MIT License.

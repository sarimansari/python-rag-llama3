# python-rag-llama3

## Overview
python-rag-llama3 is a Retrieval-Augmented Generation (RAG) system built in Python, leveraging the Llama3 language model. It combines document retrieval with generative AI to answer queries using both stored knowledge and model inference.

## Features
- Document retrieval from local sources
- Contextual response generation using Llama3
- Modular codebase for easy extension
- Simple setup and usage

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd python-rag-llama3
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare your data:**
   Place your documents in the `data/` folder (e.g., `docs.txt`).

## Usage
Run the main application:
```bash
python app.py
```
- The system will prompt for queries and return answers using retrieved context and Llama3 generation.

### Sample Requests and Responses
You can test a variety of queries:

#### AI/ML Concepts
- **Request:** What is RAG?
  **Response:** Retrieval-Augmented Generation (RAG) is a technique that combines document retrieval with text generation.
- **Request:** Explain semantic search.
  **Response:** Semantic search uses vector embeddings to find meaning beyond exact keyword matches.

#### General Knowledge Facts
- **Request:** Which company makes iPhones?
  **Response:** Apple Inc. designs iPhones, MacBooks, and other consumer electronics.
- **Request:** What is the capital of France?
  **Response:** The capital of France is Paris, known for the Eiffel Tower and rich cultural history.

#### Libraries/Tools
- **Request:** What is FAISS used for?
  **Response:** FAISS is a library developed by Facebook AI for efficient similarity search on dense vectors.
- **Request:** What does Sentence-transformers do?
  **Response:** Sentence-transformers is a Python library that provides pre-trained models for generating text embeddings.

## File Structure
- `app.py`: Main entry point for the RAG system
- `generator.py`: Handles Llama3-based text generation
- `retriever.py`: Manages document retrieval
- `data/`: Folder for source documents
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

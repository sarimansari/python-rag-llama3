from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from generator import Generator

# Load documents
with open("data/docs.txt") as f:
    docs = [line.strip() for line in f if line.strip()]

retriever = Retriever(docs)
generator = Generator()

app = FastAPI(title="RAG Demo API")

class QueryRequest(BaseModel):
    query: str
    k: int = 2

@app.post("/rag")
def rag(request: QueryRequest):
    # Step 1: Retrieve context
    context_docs = retriever.search(request.query, k=request.k)
    context = "\n".join(context_docs)

    # Step 2: Generate answer using Llama3
    answer = generator.generate(request.query, context)

    return {
        "query": request.query,
        "retrieved_context": context_docs,
        "answer": answer
    }

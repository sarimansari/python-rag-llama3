import requests

class Generator:
    def __init__(self, model="llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt, context):
        # Combine query + retrieved context
        full_prompt = f"Context:\n{context}\n\nQuestion:\n{prompt}\n\nAnswer:"
        payload = {"model": self.model, "prompt": full_prompt, "stream": False}
        response = requests.post(self.url, json=payload)
        return response.json().get("response", "")

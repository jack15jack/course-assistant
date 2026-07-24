import requests

from ai.providers.base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(
        self,
        model="llama3.1",
        url="http://localhost:11434/api/generate"
    ):
        self.model = model
        self.url = url


    def generate(self, prompt: str):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_ctx": 8192,
                    "temperature": 0.2
                }
            }
        )

        response.raise_for_status()

        return response.json()["response"]
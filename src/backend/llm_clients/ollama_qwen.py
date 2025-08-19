import os
import json

import litellm

from .base_client import BaseLLMClient

class OllamaQwenLLMClient(BaseLLMClient):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name)

    def generate_text(self, prompt):
        """Get the output from the Ollama Qwen model."""
        response = self.call(prompt)

        # Removing <think> tokens from the response
        response = response.split("</think>")[1].strip()
        
        # Assuming the response is a JSON string, we parse it
        try:
            return json.loads(response.strip("`json\n"))
        except json.JSONDecodeError:
            print("Error decoding JSON response from Qwen3. Invalid JSON format or response is in raw string format. Returning raw response.")
            return response
        except Exception as e:
            print(f"An unexpected error occurred: {e}\nReturning raw response.")
            return response
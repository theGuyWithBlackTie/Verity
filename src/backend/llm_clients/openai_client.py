import os
import json

import litellm

from base_client import BaseLLMClient

class OpenAILLMClient(BaseLLMClient):
    def __init__(self, model_name):
        super().__init__(model_name)
        litellm.api_key = os.getenv("OPENAI_API_KEY")

    def generate_text(self, prompt):
        """Get the output from the OpenAI model."""
        response = self.call(prompt)
        
        # Assuming the response is a JSON string, we parse it
        try:
            return json.loads(response.strip("`json\n"))
        except json.JSONDecodeError:
            print("Error decoding JSON response. Invalid JSON format or response is in raw string format.")
            return response
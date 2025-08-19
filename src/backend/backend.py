import yaml
import os

from llm_clients.openai_client import OpenAILLMClient
from llm_clients.ollama_qwen import OllamaQwenLLMClient

class Backend:
    def __init__(self):
        # Load configuration from YAML file
        with open(os.path.join(os.getcwd(), "app_config.yaml"), "r") as file:
            self.config = yaml.safe_load(file)

        # Initialize LLM client based on configuration
        self.main_llm_client = self.initialize_llm_client()


    def initialize_llm_client(self, which_service_llm):
        """Initialize the LLM client based on the configuration."""
        llm_name = self.config.get("llm_to_use").get(which_service_llm)
        if not llm_name:
            raise ValueError(f"LLM name for {which_service_llm} is not specified in the configuration.")
        
        # Determine the type of LLM client to use
        if "openai" in llm_name.lower():
            return OpenAILLMClient(model_name=llm_name)
        elif "qwen3" in llm_name.lower():
            return OllamaQwenLLMClient
        else:
            raise ValueError(f"Unsupported LLM client type: {client_type}")
        
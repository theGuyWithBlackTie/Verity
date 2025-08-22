import yaml
import os

from .llm_clients.openai_client import OpenAILLMClient
from .llm_clients.ollama_qwen import OllamaQwenLLMClient
from .extractors.pdf_extractor import PDFExtractor
from .extractors.docx_extractor import DocxExtractor

class Backend:
    def __init__(self):
        # Load configuration from YAML file
        with open(os.path.join(os.getcwd(), "app_config.yaml"), "r") as file:
            self.config = yaml.safe_load(file)

        # Initialize LLM client based on configuration
        self.main_llm_client = self.initialize_llm_client("main")

        # Initialize LLM client for summarization
        self.summarization_llm_client = self.initialize_llm_client("summarization")


    def initialize_llm_client(self, which_service_llm: str):
        """Initialize the LLM client based on the configuration."""
        llm_name = self.config.get("llm_to_use").get(which_service_llm)
        if not llm_name:
            raise ValueError(f"LLM name for {which_service_llm} is not specified in the configuration.")
        
        kwargs = self.config.get("llm_kwargs").get(llm_name, {})
        
        # Determine the type of LLM client to use
        if "gpt" in llm_name.lower():
            return OpenAILLMClient(model_name=llm_name)
        elif "qwen3" in llm_name.lower():
            return OllamaQwenLLMClient(model_name=llm_name)
        else:
            raise ValueError(f"Unsupported LLM client type: {llm_name}. Supported types are OpenAI and Ollama Qwen.")
        
    
    def generate_introductory_summary(self, file_paths: list[str]):
        """
        """
        

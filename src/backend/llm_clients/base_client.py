class BaseLLMClient:
    """
    Base class for LLM clients.
    This class should be extended by specific LLM client implementations.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_text(self, prompt: str) -> str:
        """
        Generate text based on the provided prompt.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
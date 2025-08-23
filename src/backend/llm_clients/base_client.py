import litellm

class BaseLLMClient:
    """
    Base class for LLM clients.
    This class should be extended by specific LLM client implementations.
    """

    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.kwargs = kwargs

    def _call(self, messages: list) -> litellm.types.utils.ModelResponse:
        """
        Call the LLM with the provided prompt.
        """
        response = litellm.completion(
            model = self.model_name,
            messages = messages,
            **self.kwargs
        )
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")

    def generate_text(self, prompt: str) -> str:
        """
        Generate text based on the provided prompt.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI


load_dotenv()


class ModelConfig:
    """Factory class to create ChatOpenAI instances for OpenCode Zen or OpenRouter models."""

    zen_models = {
        "big-pickle": "big-pickle",
        "laguna-s": "laguna-s-2.1-free",
        "nemotron-ultra": "nemotron-3-ultra-free",
    }

    openrouter_models = {
        "nemotron": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "gemini-2.0-flash": "google/deepai-googlenemotron-3ultra550b-a55b-free",
        "laguna-2.1":"poolside/laguna-s-2.1:free",
        "laguna-xs":"poolside/laguna-xs-2.1:free",
        "thinking-machine":"thinkingmachines/inkling:free",
    }

    @staticmethod
    def zen(model: str, **kwargs) -> ChatOpenAI:
        """Create a ChatOpenAI instance for OpenCode Zen models.

        Args:
            model: Model nickname or ID (e.g., "nemotron", "big-pickle")
            **kwargs: Additional arguments to pass to ChatOpenAI

        Returns:
            ChatOpenAI: Configured ChatOpenAI instance
        """
        resolved_model = ModelConfig.zen_models.get(model, model)
        return ChatOpenAI(
            model=resolved_model,
            openai_api_key=os.getenv("ZEN_API_KEY"),
            openai_api_base="https://opencode.ai/zen/v1",
            **kwargs,
        )

    @staticmethod
    def openrouter(model: str, **kwargs) -> ChatOpenAI:
        """Create a ChatOpenAI instance for OpenRouter models.

        Args:
            model: Model nickname or ID (e.g., "nemotron", "gpt-4o", "claude-3-5-sonnet")
            **kwargs: Additional arguments to pass to ChatOpenAI

        Returns:
            ChatOpenAI: Configured ChatOpenAI instance
        """
        resolved_model = ModelConfig.openrouter_models.get(model, model)
        return ChatOpenAI(
            model=resolved_model,
            openai_api_key=os.getenv("ROUTER_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            **kwargs,
        )

    @staticmethod
    def create(model: str, model_type: str = "openrouter", **kwargs) -> ChatOpenAI:
        """Create a ChatOpenAI instance.

        Args:
            model: Model nickname or ID (e.g., "nemotron", "big-pickle")
            model_type: "zen" or "openrouter"
            **kwargs: Additional arguments to pass to ChatOpenAI

        Returns:
            ChatOpenAI: Configured ChatOpenAI instance
        """
        if model_type == "zen":
            return ModelConfig.zen(model, **kwargs)
        return ModelConfig.openrouter(model, **kwargs)

    @staticmethod
    def available_zen() -> dict:
        """Return available Zen model nicknames."""
        return ModelConfig.zen_models.copy()

    @staticmethod
    def available_openrouter() -> dict:
        """Return available OpenRouter model nicknames."""
        return ModelConfig.openrouter_models.copy()
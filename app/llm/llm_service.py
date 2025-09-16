import aiohttp

from app.common.api_handlers.json_api_handler import JSONAPIHandler
from app.common.config.config import Config
from app.common.exceptions.http_exception_wrapper import http_exception
from app.llm.dto import GenerateDTO


class LLMService:
    """
    LLM service class
    Attributes:
        llm_api_handler (JSONAPIHandler): LLM API handler
    """

    def __init__(self, config: Config, llm_api_handler: JSONAPIHandler):
        """
        Initialisation function fpr LLM service class
        Args:
            config (Config): config instance to manage env configurations
            llm_api_handler (JSONAPIHandler): LLM API handler
        """

        self.__name__ = "LLMService"
        self.config: Config = config
        self.llm_api_handler = llm_api_handler

    async def get_models(self) -> list[str]:
        """
        Function to get available models from LLM API
        Returns:
            list: List of available models
        Raises:
            http_exception with response status code from LLM API
        """

        models_info = (await self.llm_api_handler.get("api/tags"))["models"]
        return [model_data["name"] for model_data in models_info] if models_info else []

    async def generate_response(self, generation_params: GenerateDTO) -> str:
        """
        Function to generate response from LLM API
        Args:
            generation_params (GenerateDTO): Generation parameters
        Returns:
            str: Generated response
        Raises:
            http_exception with response status code from LLM API
        """

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.get('LLM_API_KEY')}",
        }
        payload = {
            "model": generation_params.model,
            "prompt": generation_params.prompt,
            "stream": False,
        }
        response = await self.llm_api_handler.post(
            "/api/generate", headers=headers, data=payload
        )
        return response["response"]

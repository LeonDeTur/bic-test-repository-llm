from pathlib import Path

from app.common.api_handlers.json_api_handler import JSONAPIHandler
from app.common.config.config import Config
from app.llm.llm_service import LLMService

absolute_app_path = Path().absolute()
config = Config()
llm_api_handler = JSONAPIHandler(config.get("LLM_API_URL"))
llm_service = LLMService(config, llm_api_handler)

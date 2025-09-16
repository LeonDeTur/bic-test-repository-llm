from fastapi import APIRouter

from app.dependencies import llm_service

from .dto import GenerateDTO

llm_router = APIRouter(prefix="/llm", tags=["LLM"])


@llm_router.get("/models", response_model=list[str])
async def get_models() -> list[str]:

    return await llm_service.get_models()


@llm_router.post("/generate", response_model=str)
async def generate_text(params: GenerateDTO) -> str:

    return await llm_service.generate_response(params)


@llm_router.post("/benchmark")
async def benchmark_model():

    return {}

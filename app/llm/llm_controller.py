from fastapi import APIRouter

llm_router = APIRouter(prefix="/llm", tags=["LLM"])


@llm_router.get("/models")
async def get_models():

    return []


@llm_router.post("/generate")
async def generate_text(prompt: str):

    return {}


@llm_router.post("/benchmark")
async def benchmark_model():

    return {}

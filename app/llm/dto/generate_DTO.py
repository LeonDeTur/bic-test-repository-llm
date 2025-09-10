from pydantic import BaseModel, Field


class GenerateDTO(BaseModel):

    prompt: str = Field(..., description="The prompt to generate text from")

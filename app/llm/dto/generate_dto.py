from pydantic import BaseModel, Field


class GenerateDTO(BaseModel):

    model: str = Field(description="Model Name", examples=["llama3.2:1b"])
    prompt: str = Field(
        description="The prompt to generate text from",
        examples=["Write a poem about a cat."],
    )

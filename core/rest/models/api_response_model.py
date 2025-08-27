from pydantic import BaseModel, Field


class ApiResponse(BaseModel):
    code: int = Field(default=0)
    type: str = Field(default="unknown")
    message: str = Field(default="0")

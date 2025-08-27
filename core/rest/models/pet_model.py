from pydantic import BaseModel, Field
from typing import List
from faker import Faker
from core.rest.models.category_model import Category
from core.rest.models.tag_model import Tag
from enum import Enum

faker = Faker()


class PetStatus(str, Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class Pet(BaseModel):
    id: int = Field(default=0)
    category: Category = Field(default=Category())
    name: str = Field(default=faker.name())
    photo_urls: List[str] = Field(alias="photoUrls", default=["url1", "url2"])
    tags: List[Tag] = Field(default=[Tag()])
    status: PetStatus = Field(default=PetStatus.AVAILABLE)

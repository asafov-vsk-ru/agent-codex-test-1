from pydantic import BaseModel, Field
from faker import Faker

faker = Faker()


class Category(BaseModel):
    id: int = Field(default=0)
    name: str = Field(default=faker.name())

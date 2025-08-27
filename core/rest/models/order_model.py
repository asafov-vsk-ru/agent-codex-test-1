from datetime import datetime
from pydantic import BaseModel, Field
from faker import Faker
from enum import Enum

faker = Faker()


class OrderStatus(str, Enum):
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"


class Order(BaseModel):
    id: int = Field(default=0)
    pet_id: int = Field(alias="petId", default=0)
    quantity: int = Field(default=1)
    ship_date: datetime = Field(alias="shipDate", default=faker.date_time())
    status: OrderStatus = Field(default=OrderStatus.PLACED)
    complete: bool = Field(default=True)

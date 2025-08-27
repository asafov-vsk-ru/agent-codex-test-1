from pydantic import BaseModel, Field
from faker import Faker

faker = Faker()


class User(BaseModel):
    id: int = Field(default=0)
    user_name: str = Field(alias="username", default=faker.user_name())
    first_name: str = Field(alias="firstName", default=faker.first_name())
    last_name: str = Field(alias="lastName", default=faker.last_name())
    email: str = Field(default=faker.email())
    password: str = Field(default=faker.password())
    phone: str = Field(default=faker.phone_number())
    user_status: int = Field(alias="userStatus", default=0)

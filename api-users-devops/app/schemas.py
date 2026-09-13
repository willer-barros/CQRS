from pydantic import BaseModel, Field


class CreateUserCommand(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0)



class UserReadModel(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True
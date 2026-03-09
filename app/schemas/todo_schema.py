from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=100)
    is_done: bool = False
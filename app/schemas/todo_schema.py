from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool

    class Config:
        from_attributes = True
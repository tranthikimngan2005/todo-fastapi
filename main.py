from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# lưu todos trong RAM
todos = []

# Model dữ liệu
class Todo(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=100)
    is_done: bool = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Hello ToDo API"}


# CREATE TODO
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo


# GET TODOS (filter + search + pagination)
@app.get("/todos")
def get_todos(
    q: str = None,
    is_done: bool = None,
    limit: int = 10,
    offset: int = 0
):

    result = todos

    # search title
    if q:
        result = [t for t in result if q.lower() in t.title.lower()]

    # filter is_done
    if is_done is not None:
        result = [t for t in result if t.is_done == is_done]

    total = len(result)

    # pagination
    result = result[offset: offset + limit]

    return {
        "items": result,
        "total": total,
        "limit": limit,
        "offset": offset
    }


# GET ONE TODO
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")


# UPDATE TODO
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# DELETE TODO
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
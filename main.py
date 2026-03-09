from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# lưu todo trong RAM
todos = []

# model dữ liệu
class Todo(BaseModel):
    id: int
    title: str
    is_done: bool = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Hello ToDo API"}


# CREATE
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo


# READ ALL
@app.get("/todos")
def get_todos():
    return todos


# READ ONE
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")


# UPDATE
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
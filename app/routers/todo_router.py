from fastapi import APIRouter, HTTPException
from app.schemas.todo_schema import Todo
from app.services import todo_service

router = APIRouter()

@router.post("/todos")
def create(todo: Todo):
    return todo_service.create_todo(todo)

@router.get("/todos")
def get_all():
    return todo_service.get_todos()

@router.get("/todos/{todo_id}")
def get_one(todo_id: int):
    todo = todo_service.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}")
def update(todo_id: int, todo: Todo):
    result = todo_service.update_todo(todo_id, todo)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return result

@router.delete("/todos/{todo_id}")
def delete(todo_id: int):
    result = todo_service.delete_todo(todo_id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "deleted"}
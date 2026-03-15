from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.todo_schema import TodoCreate
from app.services import todo_service
from fastapi import BackgroundTasks
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def log_create(todo_title):
    print(f"Todo created: {todo_title}")
@router.post("/todos")
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@router.post("/todos")
def create(todo: TodoCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    background_tasks.add_task(log_create, todo.title)

    return todo_service.create_todo(db, todo)
@router.get("/todos/{todo_id}")
def get_one(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    ok = todo_service.delete_todo(db, todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "deleted"}
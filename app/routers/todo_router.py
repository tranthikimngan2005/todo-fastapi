from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.todo_schema import TodoCreate
from app.services import todo_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/todos")
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@router.get("/todos")
def get_all(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return todo_service.get_todos(db, limit, offset)

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
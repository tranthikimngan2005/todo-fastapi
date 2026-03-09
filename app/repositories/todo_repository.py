from sqlalchemy.orm import Session
from app.models.todo_model import Todo

def create(db: Session, todo):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_all(db: Session, limit: int, offset: int):
    return db.query(Todo).offset(offset).limit(limit).all()

def get_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def delete(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False
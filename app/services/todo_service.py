from sqlalchemy.orm import Session
from app.repositories import todo_repository

def create_todo(db: Session, todo):
    return todo_repository.create(db, todo)

def get_todos(db: Session, limit: int, offset: int):
    return todo_repository.get_all(db, limit, offset)

def get_todo(db: Session, todo_id: int):
    return todo_repository.get_by_id(db, todo_id)

def delete_todo(db: Session, todo_id: int):
    return todo_repository.delete(db, todo_id)
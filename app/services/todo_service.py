from app.repositories import todo_repository

def create_todo(todo):
    return todo_repository.create(todo)

def get_todos():
    return todo_repository.get_all()

def get_todo(todo_id):
    return todo_repository.get_by_id(todo_id)

def update_todo(todo_id, todo):
    return todo_repository.update(todo_id, todo)

def delete_todo(todo_id):
    return todo_repository.delete(todo_id)
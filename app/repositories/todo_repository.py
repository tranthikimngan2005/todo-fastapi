todos = []

def create(todo):
    todos.append(todo)
    return todo

def get_all():
    return todos

def get_by_id(todo_id):
    for t in todos:
        if t.id == todo_id:
            return t
    return None

def update(todo_id, todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = todo
            return todo
    return None

def delete(todo_id):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
            return True
    return False
from fastapi import FastAPI
from app.routers import todo_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(todo_router.router, prefix="/api/v1")
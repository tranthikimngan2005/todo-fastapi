from fastapi import FastAPI
from app.routers import todo_router
from app.core.database import engine
from app.models import todo_model

todo_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
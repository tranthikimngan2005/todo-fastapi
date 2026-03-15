from fastapi import FastAPI
from app.routers import todo_router
from app.auth import auth_router
from app.core.database import engine
from app.models import todo_model, user_model

# tạo bảng database
todo_model.Base.metadata.create_all(bind=engine)

# tạo app trước
app = FastAPI()

# router
app.include_router(todo_router.router, prefix="/api/v1")
app.include_router(auth_router.router, prefix="/api/v1/auth")

# health check
@app.get("/health")
def health():
    return {"status": "ok"}
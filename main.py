from fastapi import FastAPI
from app.middleware.logging_middleware import LoggingMiddleware
from app.routers import todo_router
from app.auth import auth_router

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(todo_router.router, prefix="/api/v1")
app.include_router(auth_router.router, prefix="/api/v1/auth")

@app.get("/health")
def health():
    return {"status": "ok"}
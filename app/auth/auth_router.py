from fastapi import APIRouter
from app.auth.security import create_access_token

router = APIRouter()

@router.post("/login")
def login():

    token = create_access_token({"sub": "user1"})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
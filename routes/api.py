from fastapi import APIRouter
from src.endpoints import users

router = APIRouter()
router.include_router(users.router)
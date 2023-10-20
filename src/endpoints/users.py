from fastapi import APIRouter, Body, Request, status
from typing import List
from src.model.user import User

import src.rules.users_login as login

router = APIRouter(prefix="/user", tags=["Adress"])

@router.post("/login", response_description="Login", status_code=status.HTTP_200_OK)
def login(request:Request):
    return login.login(request)
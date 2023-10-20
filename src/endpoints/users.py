from fastapi import APIRouter, Request, status

import src.rules.users_login as login

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login", response_description="Login", status_code=status.HTTP_200_OK)
def login(request:Request):
    return login.login(request)

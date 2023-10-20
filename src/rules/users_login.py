import os
import datetime
from time import timezone
from http import cookies
from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from pydantic import BaseModel

class userLogin(BaseModel):
    numero_registro: str
    senha: str

def get_collection_funcionarios(request:Request):
    return request.app.database["funcionarios"]


def login(request: Request, user: userLogin = Body(...)):
    user = jsonable_encoder(user)
    login_user = get_collection_funcionarios(request).find_one({"numero_registro": user.numero_registro})
    if login_user is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Funcionario com registro {user.numero_registro} nao existe")
    # (os.environ.get("url_mongo")
    try:
        token = jwt.encode({"exp":datetime.datetime.now(tz=timezone.utc) + datetime.datetime(day=30), "sub": login_user}, os.environ.get("SECRET"))
    except jwt.ExpiredSignatureError:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Autorização invalid, faça login novamente")
    cookies.SimpleCookie({"auth": token })
    return HTTPException(status_code=status.HTTP_200_OK, detail=f"Login successful")
    

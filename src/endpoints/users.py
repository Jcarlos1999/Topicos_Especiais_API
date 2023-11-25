from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from src.model.user import User, userLogin

import src.rules.users as user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/criar_usuario", response_description="Create User")
async def signin(request: Request, user: User = Body(...)):
    try:
        return user_controller.criar_membros(request, user)
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err}")

@router.post("/login", response_description="Login")
async def login(request:Request, user:userLogin = Body(...)):
    try:
        user_response = user_controller.login(request, user)
        return user_response # HTTPException(status_code=status.HTTP_200_OK, detail=f"{user_response}") 
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err}")
    
@router.get('/vizualizar_membros', response_description="Busca Funcionarios")
async def vizualizar_membros(resquest:Request):
    try:
        registros = user_controller.vizualizar_membros(resquest)
        return HTTPException(status_code=status.HTTP_200_OK, detail=f"{registros}")
    except Exception as err:
        print(err)

@router.post("/dados_membros", response_description="Busca Funcionario")
async def dados_membros(request: Request, body = Body(...)):
        try:
            user = user_controller.dados_membros(request, body.get('numero_registro'))
            return HTTPException(status_code=status.HTTP_200_OK, detail=f"{user}")
        except Exception as err:
             print(err)

@router.post("/delete", response_description="Delete funcionatio")
async def delete(request: Request, body = Body(...)):
    try:
        delete_user = user_controller.deletar_membros(request, body.get("numero_registro"))
        return HTTPException(status_code=status.HTTP_200_OK, detail=f"Usuario deletado: {delete_user}")
    except Exception as err:
        return HTTPException(status_code=status.HTTP_200_OK, detail=f"Usuario deletado: {delete_user}")
import os
from fastapi.encoders import jsonable_encoder
from datetime import datetime, date, timedelta
from fastapi import Body, Request, HTTPException, status
import jwt
from pymongo import MongoClient

from src.model.user import User, userLogin

def get_collection_funcionarios(request:Request):
    return request.app.database["funcionarios"]

def criar_membros(request:Request, user: User = Body(...)):
    try:   
        if get_collection_funcionarios(request).find_one({"numero_registro": user.numero_registro}):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario ja existe")
        else:
            user = jsonable_encoder(user)
            get_collection_funcionarios(request).insert_one(user)
            return HTTPException(status_code=status.HTTP_201_CREATED, detail="Funcionario Criado")
        
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao criar funcionario {err}")

def login(request: Request, user: userLogin = Body(...)):
    try:
        user_login = get_collection_funcionarios(request).find_one({"numero_registro": user.numero_registro})
        if user_login is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Funcionario com registro {user.numero_registro} nao existe")
        try:
            token = jwt.encode({"test": f"{datetime.now() + timedelta(days=3)}", "sub": f"{user_login}"}, f"{os.environ.get('SECRET')}")
        except jwt.ExpiredSignatureError:
            HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Autorização invalid, faça login novamente")
        

        return HTTPException(status_code=status.HTTP_200_OK, detail=f"Login successful {user_login}")
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao logar")
    

def dados_membros(request: Request, numero_registro = Body(...)):
    try:
        registro = get_collection_funcionarios(request).find_one({"numero_registro": numero_registro})
        if registro:
            return  registro
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Funcionario nao existe")
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao procurar funcionarion {err}")

def atualizar_membros(request: Request, user: User = Body(...)):
    try: 
        registro = get_collection_funcionarios(request).find_one({"numero_registro": user.numero_registro})
        if registro:
            get_collection_funcionarios(request).update_one(
                {"numero_registro": user.numero_registro},
                {
                    "$set": {
                    "nome": user.nome,
                    "unidade": user.unidade,
                    "ativo_unidade": user.ativo_unidade,
                    "senha": user.senha,
                    "beneficios": user.beneficios,
                    "admin": user.admin,
                    "permissoes": user.permissoes
                }
                }
            )
            return  HTTPException(status_code=status.HTTP_200_OK, detail="Funcionario atualizado")
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Funcionario nao existe")
        
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao atualizar funcionarion"+err)

def deletar_membros(request: Request, numero_registro = Body(...)):
    try: 
        delete_result = get_collection_funcionarios(request).delete_one({"numero_registro": numero_registro})
        return delete_result
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao deletar funcionarion {err}") 
def vizualizar_membros(request:Request):
    try:
        registros = get_collection_funcionarios(request).find()
        return registros
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao procurar funcionario") 
            

 
import json
import os
import bcrypt
from fastapi.encoders import jsonable_encoder
from datetime import datetime, date, timedelta
from fastapi import Body, Request, HTTPException, status
from flask import make_response
import jwt

from src.model.user import User, userLogin

salt = bcrypt.gensalt(10)

def get_collection_funcionarios(request:Request):
    return request.app.database["funcionarios"]

def criar_membros(request:Request, user: User = Body(...)):
    try:   
        if get_collection_funcionarios(request).find_one({"numero_registro": user.numero_registro}):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario ja existe")
        else:
            bytes = user.senha.encode("utf-8")
            
            hash = bcrypt.hashpw(bytes, salt)
            user.senha = hash
            user = jsonable_encoder(user)
            get_collection_funcionarios(request).insert_one(user)
            return HTTPException(status_code=status.HTTP_201_CREATED, detail="Funcionario Criado")
        
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao criar funcionario {err}")

def login(request: Request, body: userLogin = Body(...)):
    try:
        user_login = get_collection_funcionarios(request).find_one({"numero_registro": body.numero_registro})
        if user_login is None:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Funcionario com registro {body.numero_registro} nao existe")
        byte = body.senha.encode("utf-8")
        hash = bcrypt.hashpw(byte, salt)
        isEqual = bcrypt.checkpw(bytes(user_login.get("senha").encode("utf-8")), hash)
        print(user_login.get("senha").encode("utf-8"))
        print(hash)
        print(isEqual)
        if isEqual is not False:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Sua senha está incorreta")
        try:
            token = jwt.encode({"test": f"{datetime.now() + timedelta(days=3)}", "sub": f"{user_login}"}, f"{os.environ.get('SECRET')}")
            # set_cookie(request, user_login, token)
            return HTTPException(status_code=status.HTTP_200_OK, detail=f"Login successful")
        except jwt.ExpiredSignatureError:
            HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Autorização invalid, faça login novamente")
        
        return HTTPException(status_code=status.HTTP_200_OK, detail=f"Login feito com sucesso")
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao logar aqui " + str(err))
    

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
        registros = []
        for i in get_collection_funcionarios(request).find():
            registros.append(i)
        return registros
    except Exception as err:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao procurar funcionario") 
            
def set_cookie(request: Request, user = userLogin, token = str):
    user_data = {
        "registro": user.numero_registro,
    }

    user_json = json.dumps(token, user_data)
    response = make_response('User data set in cookie')
    response.set_cookie('user_info', user_json)
    return response

def get_cookie(request:Request, cookie_name):
    user_json = request.cookies.get(cookie_name)
    if user_json:
        user_data = json.loads(user_json)
        user = User(**user_data)
        return user
    else:
        return 'User data not found in cookie'
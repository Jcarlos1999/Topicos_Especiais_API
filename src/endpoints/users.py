from fastapi import APIRouter, Body, Request, status, HTTPException
from typing import List
from src.model.user import User
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

router = APIRouter(prefix="/user", tags=["Adress"])

def get_collection_users(request: Request):
    return request.app.database["users"]

def create_user(request: Request, user: User = Body()):
    user = jsonable_encoder(user)
    new_user = get_collection_users(request).insert_one(user)
    create_user = get_collection_users(request).find_one({"numero_registro": new_user.numero_registro})
    return create_user

def list_users(request: Request, limit: int):
    users = list(get_collection_users(request).find(limit = limit))
    return users

def find_user(request: Request, numero_registro: str):
    if (user := get_collection_users(request).find_one({"numero_registro": ObjectId(numero_registro)})):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {numero_registro} not found!")

def delete_user(request: Request, numero_registro: str):
    deleted_user = get_collection_users(request).delete_one({"numero_registro": ObjectId(numero_registro)})

    if deleted_user.deleted_count == 1:
        return f"User with id {numero_registro} deled sucessfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {numero_registro} not found!")

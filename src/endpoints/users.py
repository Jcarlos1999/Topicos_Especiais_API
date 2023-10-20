from fastapi import APIRouter, Body, Request, status
from typing import List
from src.model.user import User

router = APIRouter(prefix="/user", tags=["Adress"])
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class userLogin(BaseModel):
    numero_registro: str
    senha: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "examples": {
                "numero_registro":"1234",
                "senha": "4321"
            }}

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    numero_registro: str 
    nome: str
    senha: str
    unidade: str
    planos: dict  
    admin: bool
    permissoes: Optional[dict] 

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "numero_registro": "1234",
                "nome": "Renzo",
                "senha": "1234",
                "unidade": "Paraisopolis",
                "planos": {
                    "Banco": "Bradesco",
                    "Saúde": "Unimed",
                },
                "admin": True,  # Alterado para um valor booleano
                "permissoes": {
                    "Visualizar_membros": True,  # Alterado para um valor booleano
                    "Editar_informacoes": True,  # Alterado para um valor booleano
                }
            }
        }

    

    
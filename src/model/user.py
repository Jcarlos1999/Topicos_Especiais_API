import uuid
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    registro: str  # Especificar o tipo de dados do campo
    nome: str
    senha: str
    unidade: str
    ativo_unidades: bool  # Exemplo de campo booleano
    planos: dict  # Exemplo de campo dicionário
    admin: bool
    permissoes: Optional[dict]  # Campo opcional de tipo dicionário

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "registro": "1234",
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

    

    
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()
client = TestClient(app)

def test_criar_membros():
    # Testa a criação de membros
    response = client.post("/criar_membros", json={
        "numero_registro": "1234",
        "nome": "Renzo",
        "senha": "1234",
        "unidade": "Paraisopolis",
        "planos": {
            "Banco": "Bradesco",
            "Saúde": "Unimed",
        },
        "admin": True,
        "permissoes": {
            "Visualizar_membros": True,
            "Editar_informacoes": True,
        }
    })
    assert response.status_code == 200

    # Testa o caso em que o usuário já existe
    response = client.post("/criar_membros", json={
        "numero_registro": "1234",  # Este deve ser o mesmo número_registro do teste anterior
    })
    assert response.status_code == 400
    assert "Usuario ja existe" in response.text

def test_dados_membros():
    # Testa a obtenção de dados de membros existentes
    response = client.get("/dados_membros?numero_registro=1234")
    assert response.status_code == 200
    assert "nome" in response.json()

    # Testa o caso em que o membro não existe
    response = client.get("/dados_membros?numero_registro=5678")
    assert response.status_code == 400
    assert "Funcionario nao existe" in response.text

def test_atualizar_membros():
    # Testa a atualização de membros existentes
    response = client.put("/atualizar_membros", json={
        "numero_registro": "1234",
        "nome": "Renzo",
        "senha": "1234",
        "unidade": "Paraisopolis",
        "planos": {
            "Banco": "Bradesco",
            "Saúde": "Unimed",
        },
        "admin": True,
        "permissoes": {
            "Visualizar_membros": True,
            "Editar_informacoes": False,
        }
    })
    assert response.status_code == 200
    assert "Funcionario atualizado" in response.text

    # Testa o caso em que o membro não existe
    response = client.put("/atualizar_membros", json={"numero_registro": "5678", "nome": "Igor Luiz"})
    assert response.status_code == 400
    assert "Funcionario nao existe" in response.text

def test_deletar_membros():
    # Testa a exclusão de membros existentes
    response = client.delete("/deletar_membros?numero_registro=1234")
    assert response.status_code == 200
    assert "deletedCount" in response.json()

    # Testa o caso em que o membro não existe
    response = client.delete("/deletar_membros?numero_registro=5678")
    assert response.status_code == 400
    assert "Erro ao deletar funcionarion" in response.text

def test_vizualizar_membros():
    # Testa a visualização de membros
    response = client.get("/vizualizar_membros")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

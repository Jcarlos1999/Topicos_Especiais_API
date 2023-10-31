from flask import Flask, request, make_response
import json

app = Flask(__name__)

class User:
    def __init__(self, registro, nome, unidade, ativo_unidade, planos, admin, permissoes=None):
        self.registro = registro
        self.nome = nome
        self.unidade = unidade
        self.ativo_unidade = ativo_unidade
        self.planos = planos
        self.admin = admin
        if admin:
            self.permissoes = permissoes

@app.route('/set_cookie')
def set_cookie():
    user_data = {
        "registro": "1235",
        "nome": "João",
        "unidade": "PA",
        "ativo_unidade": True,
        "planos": ["Unimed", "Bradesco"],
        "admin": True,
        "permissoes": ["criar_usuario", "vizualizar_membros"]
    }

    user_json = json.dumps(user_data)
    response = make_response('User data set in cookie')
    response.set_cookie('user_info', user_json)
    return response

@app.route('/get_cookie')
def get_cookie():
    user_json = request.cookies.get('user_info')
    if user_json:
        user_data = json.loads(user_json)
        user = User(**user_data)
        return f'User Info: {user.__dict__}'
    else:
        return 'User data not found in cookie'

if __name__ == '__main__':
    app.run(debug=True)

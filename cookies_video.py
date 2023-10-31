from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Aplicativo Offline"

@app.route("/criar-cookie")
def criar_cookie():
    resposta = make_response("cookie criado")
    resposta.set_cookie("registro", "1235")
    resposta.set_cookie("nome", "João")
    resposta.set_cookie("unidade", "PA")
    resposta.set_cookie("ativo_unidade", True)
    resposta.set_cookie("planos", ["Unimed", "Bradesco"])
    resposta.set_cookie("admin", True)
    resposta.set_cookie("permissoes", ["criar_usuario", "vizualizar_membros"])
    return resposta

@app.route("/ver-cookie")
def ver_cookie():
    cookies = request.cookies
    return cookies

if __name__ == "__main__":
    app.run(debug=True)
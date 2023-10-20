import pymongo

# Conexão com o banco de dados MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.vssjehz.mongodb.net/")
db = client.APP_C213
collection = db.funcionarios

class Registro:
    def __init__(self, numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes):
        self.numero_registro = numero_registro
        self.nome = nome
        self.unidade = unidade
        self.ativo_unidade = ativo_unidade
        self.senha = senha
        self.beneficios = beneficios
        self.admin = admin
        self.permissoes = permissoes

class CRUD:
    def Criar_membros(self, numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes):
        if not collection.find_one({"numero_registro": numero_registro}):
            registro = Registro(numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes)
            collection.insert_one(registro.__dict__)
            print(f'Registro {numero_registro} criado com sucesso.')
        else:
            print(f'Registro {numero_registro} já existe.')

    def Dados_membros(self, numero_registro):
        registro = collection.find_one({"numero_registro": numero_registro})
        if registro:
            print(f'Número de Registro: {registro["numero_registro"]}')
            print(f'Nome: {registro["nome"]}')
            print(f'Unidade: {registro["unidade"]}')
            print(f'Ativo na Unidade: {registro["ativo_unidade"]}')
            print(f'Senha: {registro["senha"]}')
            print(f'Benefícios: {registro["beneficios"]}')
            print(f'Admin: {registro["admin"]}')
            print(f'Permissões: {registro["permissoes"]}')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def Atualizar_membros(self, numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes):
        if collection.find_one({"numero_registro": numero_registro}):
            collection.update_one(
                {"numero_registro": numero_registro},
                {
                    "$set": {
                        "nome": nome,
                        "unidade": unidade,
                        "ativo_unidade": ativo_unidade,
                        "senha": senha,
                        "beneficios": beneficios,
                        "admin": admin,
                        "permissoes": permissoes
                    }
                }
            )
            print(f'Registro {numero_registro} atualizado com sucesso.')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def Deletar_membros(self, numero_registro):
        if collection.find_one({"numero_registro": numero_registro}):
            collection.delete_one({"numero_registro": numero_registro})
            print(f'Registro {numero_registro} deletado com sucesso.')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def Vizualizar_membros(self):
        registros = collection.find()
        for registro in registros:
            print(f'Número de Registro: {registro["numero_registro"]}')
            print(f'Nome: {registro["nome"]}')
            print(f'Unidade: {registro["unidade"]}')
            print(f'Ativo na Unidade: {registro["ativo_unidade"]}')
            print(f'Senha: {registro["senha"]}')
            print(f'Benefícios: {registro["beneficios"]}')
            print(f'Admin: {registro["admin"]}')
            print(f'Permissões: {registro["permissoes"]}')
            print('------')

    def Dados_usuario(self, numero_registro, unidade, senha):
        registro = collection.find_one({"numero_registro": numero_registro})
        if registro:
            if registro["unidade"] == unidade and registro["senha"] == senha:
                print(f'Número de Registro: {registro["numero_registro"]}')
                print(f'Nome: {registro["nome"]}')
                print(f'Unidade: {registro["unidade"]}')
                print(f'Ativo na Unidade: {registro["ativo_unidade"]}')
                print(f'Benefícios: {registro["beneficios"]}')
            else:
                print("As informações fornecidas não correspondem ao registro.")
        else:
            print(f'Registro {numero_registro} não encontrado.')

if __name__ == '__main__':
    sistema = CRUD()

    while True:
        print("\nOpções:")
        print("1. Criar Registro")
        print("2. Ler Registro")
        print("3. Atualizar Registro")
        print("4. Deletar Registro")
        print("5. Listar Registros")
        print("6. Ler usuário por Registro, Unidade e Senha")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero_registro = int(input("Número de Registro: "))
            nome = input("Nome: ")
            unidade = input("Unidade: ")
            ativo_unidade = bool(input("Ativo na Unidade(true/false): "))
            senha = input("Senha: ")
            beneficios = input("Benefícios (separados por vírgula): ").split(',')
            admin = bool(input("Admin(true/false): "))
            if admin:
                permissoes = input("Permissões (separadas por vírgula): ").split(',')
            else:
                permissoes = []
            sistema.Criar_membros(numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes)

        elif escolha == '2':
            numero_registro = int(input("Número de Registro: "))
            sistema.Dados_membros(numero_registro)

        elif escolha == '3':
            numero_registro = int(input("Número de Registro: "))
            if collection.find_one({"numero_registro": numero_registro}):
                nome = input("Nome: ")
                ativo_unidade = bool(input("Ativo na Unidade(true/false): "))
                senha = input("Senha: ")
                beneficios = input("Benefícios (separados por vírgula): ").split(',')
                admin = bool(input("Admin(true/false): "))
                if admin:
                    permissoes = input("Permissões (separadas por vírgula): ").split(',')
                else:
                    permissoes = []
                sistema.Atualizar_membros(numero_registro, nome, unidade, ativo_unidade, senha, beneficios, admin, permissoes)
            else:
                print(f'Registro {numero_registro} não encontrado.')

        elif escolha == '4':
            numero_registro = int(input("Número de Registro: "))
            sistema.Deletar_membros(numero_registro)

        elif escolha == '5':
            sistema.Vizualizar_membros()

        elif escolha == '6':
            numero_registro = int(input("Número de Registro: "))
            unidade = input("Unidade: ")
            senha = input("Senha: ")
            sistema.Dados_usuario(numero_registro, unidade, senha)

        elif escolha == '7':
            break

        else:
            print("Opção inválida. Tente novamente.")

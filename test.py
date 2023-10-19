import pickle

class Registro:
    def __init__(self, numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes):
        self.numero_registro = numero_registro
        self.nome = nome
        self.unidade = unidade
        self.ativo_unidade = ativo_unidade
        self.senha = senha
        self.planos = planos
        self.admin = admin
        self.permissoes = permissoes

class CRUD:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.registros = {}
        self.carregar_registros()

    def carregar_registros(self):
        try:
            with open(self.arquivo, 'rb') as arquivo:
                self.registros = pickle.load(arquivo)
        except FileNotFoundError:
            self.registros = {}

    def salvar_registros(self):
        with open(self.arquivo, 'wb') as arquivo:
            pickle.dump(self.registros, arquivo)

    def criar_registro(self, numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes):
        if numero_registro not in self.registros:
            registro = Registro(numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes)
            self.registros[numero_registro] = registro
            self.salvar_registros()
            print(f'Registro {numero_registro} criado com sucesso.')
        else:
            print(f'Registro {numero_registro} já existe.')

    def ler_registro(self, numero_registro):
        registro = self.registros.get(numero_registro)
        if registro:
            print(f'Número de Registro: {registro.numero_registro}')
            print(f'Nome: {registro.nome}')
            print(f'Unidade: {registro.unidade}')
            print(f'Ativo na Unidade: {registro.ativo_unidade}')
            print(f'Senha: {registro.senha}')
            print(f'Planos: {registro.planos}')
            print(f'Admin: {registro.admin}')
            print(f'Permissões: {registro.permissoes}')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def atualizar_registro(self, numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes):
        if numero_registro in self.registros:
            registro = self.registros[numero_registro]
            registro.nome = nome
            registro.unidade = unidade
            registro.ativo_unidade = ativo_unidade
            registro.senha = senha
            registro.planos = planos
            registro.admin = admin
            registro.permissoes = permissoes
            self.salvar_registros()
            print(f'Registro {numero_registro} atualizado com sucesso.')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def deletar_registro(self, numero_registro):
        if numero_registro in self.registros:
            registro = self.registros[numero_registro]
            del self.registros[numero_registro]
            self.salvar_registros()
            print(f'Registro {numero_registro} deletado com sucesso.')
        else:
            print(f'Registro {numero_registro} não encontrado.')

    def listar_registros(self):
        for numero_registro, registro in self.registros.items():
            print(f'Número de Registro: {registro.numero_registro}')
            print(f'Nome: {registro.nome}')
            print(f'Unidade: {registro.unidade}')
            print(f'Ativo na Unidade: {registro.ativo_unidade}')
            print(f'Senha: {registro.senha}')
            print(f'Planos: {registro.beneficios}')
            print(f'Admin: {registro.admin}')
            print(f'Permissões: {registro.permissoes}')
            print(f'------')

    def leitura_usuario(self, numero_registro, unidade, senha):
        if numero_registro in self.registros:
            registro = self.registros[numero_registro]
            if registro.unidade == unidade and registro.senha == senha:
                print(f'Número de Registro: {registro.numero_registro}')
                print(f'Nome: {registro.nome}')
                print(f'Unidade: {registro.unidade}')
                print(f'Ativo na Unidade: {registro.ativo_unidade}')
                print(f'Planos: {registro.planos}')
            else:
                print("As informações fornecidas não correspondem ao registro.")
        else:
            print(f'Registro {numero_registro} não encontrado.')


if __name__ == '__main__':
    sistema = CRUD('registros.bd')

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
            planos = input("Planos: ")
            admin = bool(input("Admin(true/false): "))
            permissoes = list(input("Permissões caso for admin: "))
            sistema.criar_registro(numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes)

        elif escolha == '2':
            numero_registro = int(input("Número de Registro: "))
            sistema.ler_registro(numero_registro)

        elif escolha == '3':
            numero_registro = int(input("Número de Registro: "))
            if numero_registro in sistema.registros:
                nome = input("Nome: ")
                ativo_unidade = bool(input("Ativo na Unidade(true/false): "))
                senha = input("Senha: ")
                planos = input("Planos: ")
                admin = bool(input("Admin(true/false): "))
                permissoes = list(input("Permissões caso for admin: "))
                sistema.atualizar_registro(numero_registro, nome, unidade, ativo_unidade, senha, planos, admin, permissoes)
            else:
                print(f'Registro {numero_registro} não encontrado.')

        elif escolha == '4':
            numero_registro = int(input("Número de Registro: "))
            sistema.deletar_registro(numero_registro)

        elif escolha == '5':
            sistema.listar_registros()

        elif escolha == '6':
            numero_registro = int(input("Número de Registro: "))
            unidade = input("Unidade: ")
            senha = input("Senha: ")
            sistema.leitura_usuario(numero_registro, unidade, senha)

        elif escolha == '7':
            break    

        else:
            print("Opção inválida. Tente novamente.")

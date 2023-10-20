# import pickle

#    def Dados_usuario(self, numero_registro, unidade, senha):
#         registro = collection.find_one({"numero_registro": numero_registro})
#         if registro:
#             if registro["unidade"] == unidade and registro["senha"] == senha:
#                 print(f'Número de Registro: {registro["numero_registro"]}')
#                 print(f'Nome: {registro["nome"]}')
#                 print(f'Unidade: {registro["unidade"]}')
#                 print(f'Ativo na Unidade: {registro["ativo_unidade"]}')
#                 print(f'Benefícios: {registro["beneficios"]}')
#             else:
#                 print("As informações fornecidas não correspondem ao registro.")
#         else:
#             print(f'Registro {numero_registro} não encontrado.')
"""
Recebendo dados usuário

"""

print("Qual seu nome?")
nome = input().title()

# Processamento


# Saída de dados

print(f'Seja bem vindo(a) {nome}', '\n')
idade = int(input("Qual sua idade?\n"))

print(f'\nA idade de {nome} é {idade} e ele(a) nasceu em {2023 - idade}')

ativo = True

# print(dir(ativo))
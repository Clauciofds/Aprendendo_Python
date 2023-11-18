"""

# Refatorando uma função

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

def quadrado(num):
    return print(f'\n{num ** 2}')

# print(f'\n{quadrado(7)}')
# print(f'\n{quadrado(4)}')

quadrado(7)
quadrado(5)

# Refatorando a funcao

def cantar_parabens(aniversariante):
    print('\nParabens pra você'
          '\nNesta data querida'
          f'\nViva o {aniversariante}')

cantar_parabens('Patricia')

# Função pode ter parâmetros de entrada. Ou seja, podemos receber
# mais de uma entrada separadas com víguloa

def soma(a, b):
    return print(f'\n{a + b}')

def multipica(num1, num2):
    return print(num1 * num2)

def outra(num1, b, msg):
    return print((num1 + b) * msg)

soma(1, 2)
multipica(3, 0.5)
outra(2,2, 'Clacio')

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return print(f'Seu nome completo é {nome} {sobrenome}')

nome_completo('Claucio', 'dos Santos')

# Parâmetro são variáveis declaradas na difinição de uma função;
# Argumentos são dados passados durante a execução de função;

# Argumentos nomeados (keyoword Arguments)

# A ordem dos parêmetros e argumento sempre vão respeitar
# a definida pela função

nome = 'Claucio'
sobrenome = 'dos Santos'

nome_completo(sobrenome, nome)
nome_completo(sobrenome=sobrenome, nome=nome)
nome_completo(sobrenome='dos Santos', nome='Cleiton')
"""

def soma_impares(num):
    total = 0
    for i in num:
        if i % 2 != 0:
            total += i
    return print(f'\n{total}')

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    soma_impares(lista)


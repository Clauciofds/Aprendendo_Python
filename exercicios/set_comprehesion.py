"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""

# Exemplo 01

numeros = {num for num in range(1, 10)}
print(numeros)

# Exemplo 02

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: Transforme o código acima para transfomar em um dicionário?

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Exemplo com strings

letras = {letra for letra in 'Claucio Fernando Donizete dos Santos'}
nome = 'Claucio Fernando Donizete dos Santos'
print(len(nome))
print(letras, len(letras))

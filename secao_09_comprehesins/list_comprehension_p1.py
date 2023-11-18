"""
List Comprehension

>> Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir
   outro iterável.

# Sintaxe da List

[ dado for dado in iterárel ]

"""

# Exemplo
num = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in num]

print(res)

res1 = [numero / 2 for numero in num]

print(res1)

def funcao(valor):
    return valor * valor

res2 = [funcao(numero) for numero in num]

print(res2)

# List Comprehension versos Loop

# Loop

numeros_dobrados = []

for numero in num:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in num])

nome = 'Claucio Santos'

# 1
print([letra.upper() for letra in nome])

# 2

amigos = ['mario', 'julia', 'pedro', 'guilherme', 'vanessa']

def nome_capitular(lista):
    capitular = [amigo.capitalize() for amigo in amigos[1:]]
    return print(f'\n{capitular[0]}')

nome_capitular(amigos)


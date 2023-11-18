"""
Dictionary Comprehension

Pense no seguinte:

>> Criando Listas:
- lista = [1, 2, 3, 4]

>> Criando tuplas:
- tupla = 1, 2, 3, 4

>> Criando set (conjunto)
- conjunto = {1, 2, 3, 4}

>> Criando Dicionario
- dicionario = {'a': 1, 'b': 2, 'b':3, 'c':4}

# Sintaxe
{chave: valor for valor in interável}

"""
# Exemplo 01

numeoros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in numeoros.items()}

print(quadrado)

# Exemplo 02

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

# Exemplo 03

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
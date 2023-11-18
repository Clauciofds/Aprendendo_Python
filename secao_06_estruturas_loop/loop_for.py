"""

# Exemplo de for 1 (Iterando em strings)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre um lista)
for numero in lista:
    print(numero)

# Exemple de for 3 (Iterando sobre um range)
for numero in range(0, 10):
    print(numero)

print(len(nome))

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)
qtd = int(input('Quantos loops: \n'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'Loop desejado: {n}')
"""
nome = ' Claucio'
lista = [1, 3, 5, 7, 9]
# numero = range(1, 10)

# Original: U+1F621
# Modificado: U0001F621
num = 20

for i in range(num, 0, -1):
    print('\U0001F621 ' * i)
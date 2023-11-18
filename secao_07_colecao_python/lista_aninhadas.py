"""
Lista Aninhadas (Nested Lists)

- Algumas linguagem de programação (C/Java) possuem um estrutura de dados chamadas arrays:
   - Unidimensionais (Arrays/Vetores);
   - Multidimensionasi (Matrises):

Em Python nós temos as Listas

num = [1, 'b', 3.235, True, 5]

     __LINHA 1      __LINHA 2      __LINHA 3
    | COLUNAS |    | COLUNAS  |   | COLUNAS  |
    | |  |  | |    | |  |  |  |   | |  |  |  |
 [  [ 1, 2, 3 ],   [ 4, 5, 6 ],   [ 7, 8, 9 ]  ]

 ou seja:
 _______
 1  2  3
 4  5  6
 7  8  9
 ------
"""

# EXEMPLO
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(listas[0])
print(listas[1][2])

# Iterando com loops em um lista aninhada
for lista in listas:
    print(lista)

for lista in listas:
    for num in lista:
        print(num)

# List comprehesion
[[print(f'\n{valor}') for valor in lista] for lista in listas]

# EXEMPLO 2
tubuleiro = [[numero for numero in range(1, 5)] for valor in range(1, 4)]

print(tubuleiro)

# Gerando jogadaas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

print([['*' for i in range(1, 4)] for j in range(1, 4)])

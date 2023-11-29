"""
Faça um programa que leia um arquivo que contenha as dimensões de uma matriz
(linha e coluna), a quantidade de posições que serão anuladas, e as posições a serem
anuladas (linha e coluna). O programa lê esse arquivo e, em seguida, produz um novo
arquivo com a matriz com as dimensões dadas no arquivo lido, e todas as posições
especificadas no arquivo ZERADAS e o restante recebendo o valor 1.
Ex: arquivo "matriz.txt"

"""
import numpy as np, os
os.chdir(os.path.join("archives"))
print(os.getcwd())


# Lê o arquivo com as dimensões da matriz e as posições a serem anuladas
with open("matriz.txt", "r") as file:
    lines = file.readlines()
    rows, cols = map(int, lines[0].split())
    num_zeros = int(lines[1])
    zeros = []
    for i in range(2, num_zeros + 2):
        zeros.append(tuple(map(int, lines[i].split())))

# Cria a matriz com as dimensões dadas
matrix = np.ones((rows, cols))

# Anula as posições especificadas no arquivo
for zero in zeros:
    matrix[zero[0] - 1][zero[1] - 1] = 0

# Grava a matriz resultante em um novo arquivo
with open("matriz_resultante.txt", "w") as file:
    for row in matrix:
        file.write(" ".join(map(str, row)) + "\n")

with open("matriz_resultante.txt", "r") as file:
    print(file.readlines())
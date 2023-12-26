"""
O bloco with abre e fecha o arquivo de forma automática após o bloco with



"""

with open("texto.txt") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)

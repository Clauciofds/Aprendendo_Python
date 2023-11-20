"""
Para ler um arquivo devemos usar a função builtin open().

open -> forma simples passamos apenas um parâmetro de entrada, ou seja, o nome do arquivo, que retorna um
_io.TextIO@rapper que é o objeto que trabalhamos.

>> Para abrir um arquivo devemos usar a função builtin open().

>> Para ler o arquivo aberto usamos o função builtin read()
"""

# Exemplo
arquivo = open("texto.txt")

print(arquivo)

print(type(arquivo))

# ret = arquivo.read() # IMPORTANTE: A função retorna uma string

# Lendo arquivo
print(f"\n{arquivo.read()}")
# Observação: O sistema de leitura de arquivo usa o sistema de cursor. Desta forma todo arquivo é lido e o cursor
# para no final do arquivo.


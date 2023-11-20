"""
A função seek movimenta o curso pelo conteúdo do arquivo

Para ler um arquivo devemos usar a função builtin open().

open -> forma simples passamos apenas um parâmetro de entrada, ou seja, o nome do arquivo, que retorna um
_io.TextIO@rapper que é o objeto que trabalhamos.

read -> usamos para ler o conteúdo de um arquivo aberto

close -> IMPORTANTE que devemos fechar o arquivo após editarmos o arquivo
         e se necessário verificar o status do arquivo com a função closed.
         Quando o arquivo é aberto o sistema reconhece como um arquivo de streming que
         está sendo edita por algum usuário ou operação.

"""
from colorama import Fore

arquivo = open("texto.txt")

print(arquivo.read())

arquivo.seek(0)

print(f"\n{Fore.LIGHTGREEN_EX}{arquivo.read()}")

arquivo.seek(25) # Coloquei o cursor na posição 25 para elimanar a primeira linha do texto do arquivo
print(f"\n{Fore.LIGHTBLUE_EX}{arquivo.read()}")

print(Fore.RESET)

arquivo.seek(0)
print(arquivo.readline()) # Lê a linha onde o curso se localiza após a leitura do arquivo

linhas = arquivo.readlines()# + arquivo.readline()

print(linhas, len(linhas), type(linhas))

print(linhas[1].split(" "))

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)

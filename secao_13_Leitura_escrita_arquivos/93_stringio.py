"""
 O StringIO

 Nos da permissão, quando necessário para:

 Ler o arquivo e/ou;
 escrever no arquivon

 Tudo isso na memória da máquinva



"""

from io import StringIO

mensagem = "Este é apenas uma string normal"

# Criando um arquivo na memoria com a string contida na variável.
arquivo = StringIO(mensagem)
# arquivo = open(arquivo.read())

print(arquivo.read())

arquivo.write("\nOutro texto")

arquivo.seek(0)
print(f"\n{arquivo.read()}")

arquivo.seek(0)
arquivo.write("Título.")

arquivo.seek(0)
print(f"\n{arquivo.read()}")

arquivo.close()

print(arquivo.closed)


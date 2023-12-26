"""
r -> Abre arquivo para leitura.
w -> Abre para escrita. ATENÇÃ0: Se o arquivo existe ele sobrescreve o conteúdo.
x -> Abre para escrita se o arquivo existir.
a -> Abre para escrita no final do arquivo e se o arquivo não existir vai ser criado.

http://docs.python.org/3/library/functions.html#open

try:
    with open("sys/conteudo.txt", "x") as arquivo:
        arquivo.write("Teste de conteúdo. \n")
except FileExistsError as err:
    print(f"{err}\n")

with open("modificado/lista_compras.txt", "a") as arquivo:
    while True:
        item = input("Acrescenta a lista de compras:\n"
                     "Ou s para sair: ")
        if item != "s" and item != "S":
            arquivo.write(f"{item}\n")
        else:
            break




"""

with open("modificado/templates/arquivo.txt", "r+") as arquivo:
    conteudo = arquivo.read()
    arquivo.seek(0)
    arquivo.write("Sumario\n\n" + conteudo)

with open("modificado/templates/arquivo.txt") as texto:
    print(texto.read())

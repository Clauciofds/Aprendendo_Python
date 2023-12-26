"""
Quando vamos escrever em um arquivo usamos a função with open("nome_arquivo", "w")
podem assim ler com read e editar o mesmo.

Obs: Se exitir o arquivo o conteúdo será sobrescrito. Cuidado
     Se o arquivo ainda não existir o mod "w" cria o arquivo com a extenção desejada.

with open("frutas.txt", "a") as arquivo:
    while True:
        fruta = input("Qual fruta na lista\n"
                      "Ou digite S para sair: ")
        if fruta != "s" and fruta != "S":
            arquivo.write(f"{fruta}\n")
        else:
            break




"""
with open("novo.txt", "w") as arquivo:
    arquivo.write("Acrescentando conteúdo ao fim do arquivo texto.txt...\n"
                  "\nFIM DO TEXTO")

with open("novo.txt") as arquivo:
    print(arquivo.read())



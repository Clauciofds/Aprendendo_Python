"""
O operador Walrus permite fazer a atribição e retorno de valor em uma única expressão.


variavel := expressão


"""

# nome = "Claucio"
#
# print(nome)
#
# print(nome1 := "Cleiton Santos")

# # Python 3.7
# cesta = []
# fruta = input('Fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Fruta: ')

# Python 3.8
cesta: list = []
while (fruta := input('Fruta: ')) != '' and (opcao := input('Continua y or n: ')) == 'y':
    cesta.append(fruta)


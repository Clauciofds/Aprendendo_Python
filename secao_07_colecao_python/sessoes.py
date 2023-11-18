lista_num = [1, 2, 5, 65, 34, 54, 31, 44, 45, 10, 2, 5]
pesquisa = int(input('Busca: '))

# Lista para armazenar as posições onde o número 2 aparece
posicoes = []

for index, value in enumerate(lista_num):
    if value == pesquisa:
        posicoes.append(index)

quantidade_de_2 = len(posicoes)

print("O número", pesquisa,"aparece", quantidade_de_2, "vezes na lista nas posições:", posicoes)


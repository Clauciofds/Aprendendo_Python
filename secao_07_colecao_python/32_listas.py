lista = 'Claucio Fernando'

lista1 = list(lista)

print(lista1)

letra = 'b'
if letra in lista1:
    print(f'Encontre "{letra}" na lista.')
else:
    print(f'Não encontrei nada')

# print(dir(lista))

lista_num = [1, 2, 5, 65, 34, 54, 31, 44, 45, 10, 2, 5]

print(lista_num)

print(sorted(lista_num))

print(lista_num)

'''
Para adicionar um elemento em lista utiliza-se o append

OBS: Apenas um elemento por comando, mas pode-se inserir outros dados em tipos de lista
'''

# lista2.append([4, 7, 2])

# print(lista2)

# lista2.extend([234, 7, 8])
# print(lista2)

# lista2.extend('Claucio')
# print(lista2)

# Pode-se inserir um novo elemento infomando a posição do elemento na lista usando um índice

# lista2.insert(2, 'Santos')
# print(lista2)

# print(lista2[::-1])
# Desta forma na lista mista vai dar erro - sorted(lista2, reverse=True)

# Para remover o último elementos usa-se pop()
# Colocando um índice entre os parenteses serão eleminados
# lista2.pop(2)
# print(lista2)

# Podemos limpar a lista com comando lista.clear()

lista *= 3
print(lista)

# i = (lista2[1])*3
# print(type(i))
# lista2.pop(1)
# lista2.insert(1, i)
# print(lista2)

lista = 'Claucio Santos'
print(lista)
lista1 = lista.split()
print(lista1)
lista3 = list(lista1)[0]
print(type(lista3))
print(lista3)
lista3 = list(lista3)
print(type(lista3))
print(lista3)

lista3 = '-'.join(lista3)
print(lista3)

lista2 = [2, 4, 4]

soma = 0
for elementos in lista2:
    print(elementos)
    soma += elementos
print(soma)

# Criando lista com variáveis e usando while/for
carrinho = []
produto = ''

# while produto != 's':
#     print("Adicionar um produto na lista ou digite 's' para sair")
#     produto = input()
#     if produto != 's':
#         carrinho.append(produto)
#
# for produto in carrinho:
#     print(produto)

# Fazendo acesso aos elementos indexada
cores = ['azul roxo', 'vermelho', 'verde', 'amarelo']

for indice, cor in enumerate(cores):
    print(indice, cor)

cor = list(enumerate(cores))
print(cor)
print(cor[1][1])

nova_lista = cores.index("vermelho")
print(nova_lista)

lista_de_cores = [(0, 'azul'), (1, 'vermelho'), (2, 'verde'), (3, 'vermelho')]
# cor_procurada = 'vermelho'
#
# print(len(lista_de_cores))
# i = 0
#
# while i < len(lista_de_cores):
#     indice_cor = next(index for index, cor in lista_de_cores if cor == cor_procurada)
#
# print("O índice da cor vermelha é:", indice_cor)

nome = lista.split()
print(nome)

# Transformando um lista em string
nome_lista = ' '.join(nome)
print(nome_lista)

# slace de str de um lista
print(cores[-1])

# slace de um lista de um lista
print(cores[-1:])

print(lista_de_cores[-1:])

print(lista_num)
print(lista_num[1:-1])
print(lista_num[::2])
print(lista_num.index(2))
print(lista_num.index(2, 2))
print(cores[::-1])

print(len(lista_num))
print(max(lista_num))
print(sum(lista_num))
print(lista_num.count(5))

# Desempacotamento de lista
numeros = [1, 2, 3]
num1, num2, num3 = numeros

print(num1)
print(num2)
print(num3)
print(numeros)

nov_numeros = numeros.copy()
print(nov_numeros)

nov_numeros.append(4)
print(nov_numeros)
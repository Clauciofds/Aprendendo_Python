"""
Zip

zip() -> Cria um iterável (zip object) que agrega elemento de cada iterável passados como entrada 
em pares.

"""
from colorama import Fore
from statistics import mean
# Exemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(Fore.BLUE)

print(zip1)
print(type(zip1))

# Sempre podemos gerar um lista, tupla, ou dcionário
zip2 = list(zip(lista1, lista2, 'abc'))
print(f'Lista: {list(zip2)}')
print(f'tupla: {tuple(zip2)}')
print(f'set: {set(zip2)}')
print(f'dicionário: {dict(zip1)}')

print(f'\n{Fore.LIGHTGREEN_EX}')

lista3 = [7, 8, 9, 10, 11]

zip3 = zip(lista1, lista2, lista3)
print(list(zip3))

print(f'\n{Fore.LIGHTRED_EX}')

tupla = 1, 2, 3, 5, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e':15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(f'\n{list(zip(*dados))}')

# Exemplo de list comprehension

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos =['Maria', 'Pedro', 'Carla']

print(f'\n{Fore.LIGHTCYAN_EX}')

final = {dado[0]: mean(dado[1:]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos usar o map()

final1 = zip(alunos, map(lambda nota: mean(nota), zip(prova1, prova2)))

print(list(final1))

print(Fore.RESET)
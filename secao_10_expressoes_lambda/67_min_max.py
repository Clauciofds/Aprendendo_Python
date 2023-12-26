"""
Min Max

max() - Retorna o maior valor de um interável ou maior de dois mais elementos.

"""

from colorama import Fore

lista = [1, 8, 3, 2, 34, 0]
tupla = 1, 8, 3, 2, 34, 0
conjunto = {1, 8, 3, 2, 34, 0}
dicionario = {'a': 1, 'b': 8, 'c': 3, 'd': 2, 'e': 34, 'f': 0}

print(max(lista))
print(max(tupla))
print(max(dicionario))
print(max(dicionario.values()))

print('')

# Faça um programa que receba dois valores do usuário e mostre o maior.

# val1 = int(input('Informe um valor: '))
# val2 = int(input('Informe outro valor: '))
#
# print(max(val2, val1))

print(f"\n{Fore.LIGHTRED_EX}{max('Claucio Santos')}")

# min()
print('')
print(min(lista))
print(min(tupla))
print(min(dicionario))
print(min(dicionario.values()))

print('')

# Faça um programa que receba dois valores do usuário e mostre o maior.

# val1 = int(input('Informe um valor: '))
# val2 = int(input('Informe outro valor: '))
#
# print(min(val2, val1))

print(f"\n{Fore.LIGHTCYAN_EX}{min('Claucio')}")

# Outros exemplo
print(Fore.GREEN)
nomes = ['Arya', 'Sanson', 'Dora', 'Tim', 'Ollivander']
numeros = 1, 2, 3

print(max(nomes)) # Tim
print(min(nomes)) # Arya
print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim
print(max(len(nomes), len(numeros)))
print(max(nomes, numeros, key=len))

print(f'\n{Fore.YELLOW}')

musicas = [
    {"titulo": "Thuderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO - Imprimir apenas o título da música
print(f'\n{Fore.LIGHTCYAN_EX}')
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFI0 - Imprimir a música mais tocada e a menos tocada sem usar max(), min() ou lambda.
print(f'\n{Fore.LIGHTBLUE_EX}')
"""
Criaando a variáveis para determinar ordenação e minímos e máximos da lista dada
"""
ordenacao = []
maior = 0
menor = len(musicas)
titulo_musica = ""

# Percorrer a lista de músicas e determina o título da mais tocada.
for musica in musicas:
    if musica['tocou'] > maior:
        maior = musica['tocou']
        titulo_musica = musica['titulo']

# Perorre a lista de música e determina o títuloa da menos tocada.
for musica in musicas:
    if musica['tocou'] < menor:
        menor = musica['tocou']
        titulo_musica = musica['titulo']

# Percorre o dicionário de músicas e cria um lista para ordenação e identificar o maior e o menor sucesso da dicionário.
for musica in musicas:
    ordenacao.append(musica['tocou'])

ordenacao.sort()

# Exibir o resultado
print(f"A música mais tocoda: {titulo_musica} {ordenacao[-1]} vezes")
print(f"A música menos tocada: {titulo_musica} {ordenacao[0]} vezes")

teste = max(musicas['tocou'].values())
print(teste)
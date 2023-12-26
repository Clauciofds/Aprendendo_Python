"""
Sorted
Não confunda com a função sort(), o sorted() podemos utilizar com qualquer iterável.

"""

# Exemplo

numeros = 6, 1, 8, 2
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior
print(numeros)

# Adicionando parâmetros aso sorted()
print(f'\n{sorted(numeros, reverse=True)} {numeros}')

# Usamos o sorted() mais complexas
print('')
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carls", "tweets": ["Eu gosto de gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu adoro de cachorros", "Eu adoro pizzas"]},
    {"username": "doggo", "tweets": ["Eu adoro bolos", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

print(f'\nOrdem alfabética\n{sorted(usuarios, key=lambda usario: usario["username"])}')

print(f'\n2 {sorted(usuarios, key=lambda usario: usario["username"], reverse=True)}')

musicas = [
    {"titulo": "Thuderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32},
]

from colorama import Fore

# Ordenação crescente das tocada
print(f"\n{Fore.BLUE}+ tocadas {sorted(musicas, key=lambda musica: musica['tocou'])}")

# Ordenação decrescente das tocadas
print(f"\n- tocadas {Fore.RESET}{sorted(musicas, key=lambda musica: musica['tocou'], reverse=True)}")


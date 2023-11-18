"""
Generators

Por que se chama generators
"""

# Poderiamos ter feiro utilizando generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Kassio']

print(any([nome[0] == 'C' for nome in nomes]))

res = (nome[0] == 'C' for nome in nomes)
print(type(res))

print('')

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

print('')

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# getsizeof()? -> Mostra quantos bytes um objeto ocupa em memória
from sys import getsizeof

print('')
print(f"Tamanh de 'Geek'   {getsizeof('Geek')}")
print(f"Tamanh de 91       {getsizeof('91')}")
print(f"Tamanh de 1000000  {getsizeof('1000000')}")
print(f"Tamanh de 1000001  {getsizeof('1000001')}")
print(f"Tamanh de True     {getsizeof(True)}")

print('')
# Gerando um lista de números com list comprehesion
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista com Set Comprehesion
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista com Dictionary Comprehesion
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando um lista com Generator
gen = getsizeof(x * 10 for x in range(1000))

print(f'LIst Comprehesion:        {list_comp} bytes')
print(f'Set Comprehesion:         {set_comp} bytes')
print(f'Dictionary Comprehesion:  {dic_comp} bytes')
print(f'Generator Expression:     {gen} bytes')

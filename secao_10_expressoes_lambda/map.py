"""
Map

Com map fazemos mapeamento de valores para função.

"""

from math import pi as pi


def area(r):
    """Calcula a área de um circulo com raio 'r'."""
    print(round(pi * (r ** 2), 2))
    return round(pi * (r ** 2), 2)

area(2)
area(5.3)

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []

for r in raios:
    areas.append(area(r))

# Usando Map

areas = map(area, raios)
print(areas, type(areas))
# print(list(areas))

# Usando o map com lambda

print(list(map(lambda r: round(pi * (r ** 2), 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

# Exemplo 01

cidades = [
           ('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 29), ('Los Angeles', 26),
           ('Tokio', 27), ('Nova York', 10), ('Londres', 5)
]

# Transformando as temperaturas em farenite: f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], round((9/5) * dado[1] + 32, 1))

print(list(map(c_para_f, cidades)))

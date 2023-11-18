from numpy import square
from math import pi

raio_da_esfera = float(input('Digite o raio da esfera: '))

def calcular_volume_esfera(raio_da_esfera=0):
    volume_esfera = 4 / 3 * pi * square(raio_da_esfera)
    return print(f'\nO volume da esfera é = {volume_esfera:.20f} mm')

calcular_volume_esfera(raio_da_esfera)
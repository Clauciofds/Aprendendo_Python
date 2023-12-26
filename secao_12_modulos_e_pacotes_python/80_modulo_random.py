"""
Módulos python são os outros arquivos cliado na mesma pasta ou pastas diferentes.

O random tem a função de criar números pseudo-aleatório.

print(rd.random())
print(dir(rd))

# EXEMPLO 02 - IMPORTANDO APENAS AS FUNÇÓES QUE IREMOS UTILIZAR DA BIBLIOTECA RANDOM
from random import random as rd

print(f'\n{fc.LIGHTBLUE_EX}{rd()}\n')

for i in range(10):
    print(f'{fc.LIGHTRED_EX}{rd()}')


for i in range(10):
    print(f'{fc.LIGHTCYAN_EX}{round(rd() * 10, 2)}')


"""

# EXEMPLO 01 - IMPORTANDO TODA BIBLIOTECA RANDOM

from random import (uniform, randint, sample, choice, shuffle) # lista usadas no exercícios: random(), uniform()
from colorama import Fore as fc

for i in range(5):
    print(round(uniform(0, 2), 2))

print('')

for i in range(15):
    print(randint(1, 25), end=', ')

loto = sample(range(1, 25), 15)
loto.sort()

print(f'\n{loto}')

# choice() mostra um valor aleatório entre um iterável.

papeltesoura = ['pedra', 'papel', 'tesoura']

print(choice(papeltesoura))

# shuffle embaralha os dados.

cartas = ['AS', '2', '3', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(cartas)
shuffle(cartas)
print(cartas[0]) # ou podemos usar o pop e assim ir eliminando as opções do baralho. Ex: cartas.pop()


print(fc.RESET)
# Faça um program que leia um número inteiro e o imprima.
num = 34
# print(dir(num))
print(num)
print(type(num))

# Faça um programa que elia um número real e o imprima.
num = 34.3
print(f'\n{type(num)}')
print(num)
num = int(num)
print(type(num))
print(num)

# Peça ao usuário digitar três números inteiros
num1 = int(input('\nDigite três valores inteiros: '))
num2 = int(input('Digite três valores inteiros: '))
num3 = int(input('Digite três valores inteiros: '))
print(f'A soma é: {sum([num1, num2, num3])}')

# Leia um número real e imprima a raiz quadrada do mesmo.
# num = num1**2
print(f'\nA raiz quadrada do primeiro número é: {num1**2}')

# Leia um número real e leia a quinta parte do mesmo.
print(f'\nA quintal parte do segundo número é: {num2/5}')

# Leia um temperatura em C° e apresente-a convertida em F°, sendo a fórmula F°=C°*(9,0/5,0)+32
c = float(input(f'\nDigite a temperatura e C° para converter e F°: '))
# print(c, type(c))
print(f'A Temperatura e F° é de: {c*(9.0/5.0)+32}°')

"""
A importância de R$ 780.000,00 será divida entre ganhadores de um concorso. Sendo que da
quantia total:
- 46%
- 32%
- e o restante.
"""

premio = float(780000)
print(f'O prémio que será distrituidos para os ganhadores será de: R$ {premio:,.2f}')

premio1 = float(premio * 0.46)
premio2 = float(premio * 0.32)
premio3 = float(premio - (premio * 0.46 + premio * 0.32))

print(f'\nO primeiro receberá R$ {premio1:,.2f}',
      f'\nO segundo receberá R$ {premio2:,.2f}',
      f'\nO terceiro receberá R$ {premio3:,.2f}',
      f'\nTeste da divisão é R$ {sum([premio1, premio2, premio3]):,.2f}')

from math import hypot
a = float(input('\nQual comprimento do cateto oposto: '))
b = float(input('Qual comprimento do cateto adjacente: '))
hi1 = (a ** 2 + b ** 2) ** 0.5
hi2 = hypot(a, b)

print('No calculo manual com python: {:.2f}'.format(hi1))
print('Com importação da classe math é: {:0>5.2f}'.format(hi2))

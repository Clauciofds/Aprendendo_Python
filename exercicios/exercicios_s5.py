"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1 == num2:
    print(f'Os números são iguais: {num1} = {num2}')
elif num1 > num2:
    print(f'Primeiro número é maior que o segundo. {num1} > {num2}')
else:
    print(f'O segundo número e maior que o primeiro. {num2} > {num1}')
"""

from math import sqrt

num = 0

while True:
    num = int(input('Digite um número: '))

    if num >= 0 and sqrt(num).is_integer():
        print(f'A raiz quadra é: {sqrt(num):.2f}')
        break
    elif sqrt(num) % 2 != 0:
        print(f'O número {num} não tem uma raiz com número inteiro!')

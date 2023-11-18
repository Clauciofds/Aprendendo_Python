import random

a = random.randrange(0, 101)
b = random.randrange(0, 101)
chute = -1

# print(a, b)

soma = a + b

# print(soma)

while chute != soma:
    chute = int(input(f'\nQual é o resultado da soma de {a} + {b} ? '))
    if chute != soma:
        resp = input(f'\nVocê errou. Que pena!!!\n'
                     f'Quer tentar de novo?\n'
                     f'Você tem outra chance Sim(S) ou Não(N)? ')

        resp = resp.upper()
        if resp == 'N':
            print(f'\nA soma é {soma}.')
            break
    elif chute == soma:
        print(f'\nVocê acertouu. Parabéns!!!',)


from numpy import sqrt

num = int(input('Digite um número inteiro: '))

def quadrado_perfeito(num):
    raiz = int(sqrt(num))
    if sqrt(num) % 2 == 0:
        return print(f'\nA raiz quadrada'
                     f' do {num} é {raiz}')
    return print(f'O {num} não possui raiz quadrada perfeita')

quadrado_perfeito(num)
from numpy import sqrt, square

def hipotenusa(a=0, b=0):
    lados = []
    hipo = 0

    for i in range(2):
        while True:
            lado = float(input('Digite valor do cateto do triângulo: '))
            if lado >= 0:
                lados.append(lado)
                break
            else:
                print('Digite um número positovo!')


    a = lados[0]
    b = lados[1]
    hipo = sqrt(square(a) + square(b))
    return print(f'\nA hiponenusa do triangula: {hipo:.2f}')

hipotenusa()
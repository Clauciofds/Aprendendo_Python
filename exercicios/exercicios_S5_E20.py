from numpy import square as qd

lados_triangulo = []

for i in range(3):
    while True:
        lado = float(input('Digiti a dimensãos de um dos lados do triangulo: '))
        if lado >=1:
            lados_triangulo.append(lado)
            break
        else:
            print('Digite um número positivo\n')

lados_triangulo.sort(reverse=True)

a = lados_triangulo[0]
b = lados_triangulo[1]
c = lados_triangulo[2]

# print(a, b, c)

print('')

if a == b and a == c:
    print('Este triângulo é EQUILÁTERO')
elif qd(a) == qd(b) + qd(c):
    print('Este é um TRIÂNGULO RETÂNGULO ')
elif a == b or a == c or b == c:
    print('Este triângulo é ISÓSCELES')
else:
    print('Este triangulo é ESCALENO')
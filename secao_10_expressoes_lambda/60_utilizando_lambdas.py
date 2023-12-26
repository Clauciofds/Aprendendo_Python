"""
Utilizando lambdas

Conhecidas por Express'oes Lambdas, ou simplesmente Lambdas, são funçoes sem nome, ou
seja funções anònimas.

"""

# Exemplo 01 - Função Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Exemplo 02 - Expressão Lambda
lambda x: 3 * x + 1

# e como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múpliplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', ' JOLIE '))

# Exemplo 03

amar = lambda: 'Como nao amor Python'

uma = lambda x: 3 * x + 1

dois = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x1, ..., xn: <expressao>

print(amar())
print((uma(6)))
print(round(dois(5, 7)))
print(round(tres(3, 5, 8)))

# OBS: Se passaramos mais argumentos do que parâmetros esperados teremos TypeError

# Exemplo 04

autores = [
    'Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
    'Douglas Adams', 'M. G. Wells', 'Leigh Brackett'
]

print(autores)

# Uso adquado da expressao lambda

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Exemplo de função quadratica com uso da expressão lambda.

# f(x) = a * x ** 2 + b * x + c

# Definindo a Funcao

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x**2 + b * x + c"""
    return lambda x: a * x**2 + b * x + c

resultado = geradora_funcao_quadratica(2, 3, -5)

print(resultado(0))
print(resultado(1))
print(resultado(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
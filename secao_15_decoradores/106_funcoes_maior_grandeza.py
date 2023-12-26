"""
Funções de Maior Grandeza - Higher Order Functions - HOF

- Quando um linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
nos nossos pogramas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, em inglês - First Class Citizen

"""
from colorama import Fore

# Definindo as funções
def somar(a, b):
    return f'{float(round(a + b, 2)):>4}'


def diminuir(a,b):
    return f'{float(round(a - b, 2)):>4}'


def multiplicar(a, b):
    return f'{float(round(a * b, 2)):>4}'


def dividir(a, b):
    return f'{float(round(a / b, 2)):>4}'


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Executar as funcoes
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# calcular(4, 3, somar)
# calcular(4, 3, diminuir)
# calcular(4, 3, multiplicar)
# calcular(4, 3, dividir)

# Nested Functions
"""
Em Python podemos ter funções dentre de funçõas:
- Nested Functions
- Inner (Funçoes Internas)
"""

from random import  choice

print(Fore.RED)


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Joao'))
print(cumprimento('Joana'))

print(Fore.LIGHTBLUE_EX)


def faz_me_rir():
    def rir():
        return choice(('hhhhhhhh', 'iiiiiiiii', 'akakakakakak'))
    return rir


rindo = faz_me_rir()
print(rindo())

print(Fore.LIGHTGREEN_EX)

# Inner Functions podem acessar o escopo de funções mais externas.
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahah', 'kkkkkkkkkkkkk', 'riririrriririri'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
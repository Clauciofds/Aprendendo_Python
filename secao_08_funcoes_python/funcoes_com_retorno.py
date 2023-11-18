num = [1, 2, 3]

ret_pop = num.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(num)

print(f'Retorno de print: {ret_pr}')

# EXEMPLE 01
def quadrado_de_7():
    print(f'\n{7 * 7}')

print(quadrado_de_7())

ret = quadrado_de_7()

print(f'Retorno: {ret}')

# Vamos REFATORAR função acima para que ela retorne um valor

def raiz_de_7():
    return 7 * 7

ret = raiz_de_7()

print(f'\nRetorno: {ret}')
print(f'\nRetorno: {raiz_de_7()}')

# Refatorando a função diz_oi()

def diz_oi():
    return 'Oi!'

diz_oi() # Desta forma não temos nenhuma saída é nessário acrescentar a função print()

alguem = '  Pedro'

print(diz_oi() + alguem)

print('')
# O return finaliza a função
def dis_oi():
    print('Estou sendo executado antes de return')
    return 'Oi!'

# dis_oi()
print(dis_oi())

# EXEMPLO 2
def nova_funcao():
    variavel = False # OPCOES: True, None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(f'\n{nova_funcao()}')

# EXEMPLO 3

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(f'\n{outra_funcao()}')
print(type(outra_funcao()))
print(sum(outra_funcao()))
print(outra_funcao()[1])

# FUNÇÃO PARA TIRAR CARA OU COROA

from random import random

def joga_moeda():
    # Gera um número pseudo-rondômico entre 0 e 1
    if random() >= 0.5:
        return print(f'\nCara')
    return print(f'\nCoroa')

joga_moeda()
joga_moeda()


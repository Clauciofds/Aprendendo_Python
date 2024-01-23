"""
Assertions (Afirmações/Checagenens/Questionamento)

Em python é utilizada a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.


>>                          ALERTA                           <<
Se um programa for executada em -O todas suas validações
serão ignoradas, ou seja, seu código com assset será ignorado...

"""

def soma_numero_positivo(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return print(a + b)

ret = soma_numero_positivo(2, 4)  # Resutado esperado 6
# ret = soma_numero_positivo(-2, 6)  # Resultado esperado AssertionError

def definir_nome(nome):
    assert isinstance(nome, str), 'Nome deve ser uma str'
    return nome

nome1 = definir_nome("claucio")  # Resultado esperado verde
# nome2 = definir_nome(3)  # Resultado esperado AssertionError - vermelho
print(nome1)

print('')

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'chocolate'
    ], 'A comida dever ser fast food'
    return f'Eu estou comendo {comida}'

comida = input("Comida: ")
print(comer_fast_food(comida))

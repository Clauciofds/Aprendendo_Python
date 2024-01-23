"""
Para rodar um test devemos intruduzir no código '>>>'

e para rodar o teste em questão no console deve-se digitar a seguinte linha:

python -m doctest -v nome_do_modulo.py

def soma(a, b):
    soma os números a e b
    # >>> soma(1, 2)
    3
    # >>> soma(4, 6)
    10

    return a + b

RESULTADO:

Trying:
    soma(4, 6)
Expecting:
    10
ok
1 items had no tests:
    doctests
1 items passed all tests:
   2 tests in doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.



"""


# EXEMPLO TDD

# def duplicar(valores):
#     """duplicar os valores em uma lista
#     :param valores:
#     :return: Any
#
#     >>> duplicar([1, 2, 3, 4])
#     [2, 4, 6, 8]
#
#     >>> duplicar([])
#     []
#
#     >>> duplicar(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']
#
#
#     >>> duplicar([True, None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * elemento for elemento in valores]


# EXEMPLO DAS ASPAS SIMPLES E DUPLAS NO DOCTEST
# def fala_oi():
#     """Fala oi
#     :return: str "oi"
#
#     >>> fala_oi()
#     'oi'  # As aspas só será reconhecidas se estiver com as simples
#     """
#     return "oi"


# EXEMPLO 03
def verdade():
    """Reorna verdade

    >>> verdade()
    True
    """
    return True

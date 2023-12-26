"""
Pacote -> É um diretório contendo uma coleção de módulos;

OBSERVAÇÃO:
Nas versões do Python 3.x, não é mais obrigatório a utilização de um arquivo __init__.py para especificar
um pacote, mas mantem-se para continuar compativel com versões anteriores.

"""

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

"""
PEP8 - Python Enhacement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

Á ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

[2] - Utilize nome em minúsculo, separados por underline para funções ou variáveis;
"""


class Calculador:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

"""
[3] - Utilize 4 espaços para identação! (NÃO USE O A TECLA TAB PARA IDENTAÇÃO)
"""

if 'a' in 'banana':
    print('Tem')

"""
[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco:
- Métodos dentro de um classe devem ser separadas por um linha em branco:

[5] - Imports
- Deve devem ser sempre escritos em linhas separadas;
"""

# Import Errado

import sys, os

# Import Correto

import sys
import os

"""
Debunggando com PDB

PDB -> Python Debugger



"""


# def dividir(a, b):
#     print(f'a={a}, b={b}')
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError, NameError) as err:
#         return f'Ocorreu um problema: {err}'
    
# print(dividir(4, 0))

"""
Existem formas mais profissionais de se fazer um debug, utilizando o debugger
Em python, podemos fazer isso em diferentes IDEs, como o ou utilizando o PDB - Python Debugger
"""


# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError, NameError) as err:
#         return f'Ocorreu um problema: {err}'
    
# print(dividir(4, 2))

# Uzando o pdb
# Lista de comando do PDB
# l (lista onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)
"""
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python Essencial'
final = nome_completo + 'faz curso' + curso
print(final)

"""

# confitros com os comando de pdb
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# para resolver o conflito do código possuir os mesmo nomes, utilize o comando p para resover


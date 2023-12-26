"""
Tipo string

Em python, um dado é considerado do tipo strint sempre que estiver entre aspas
"""

nome = 'Claucio Fernando'
teste = [('a', 'b', 'c'), ('d', 'e', 'f')]

num = '43'

print(type(num))
print(num)

num = float(num)
print(f'\n{type(num)}')
print(num)

num = int(num)
print(f'\n{type(num)}')
print(num)

num = str(num)
print(f'\n{type(num)}')
print(num)

print(f'\n{nome}')
print(nome.split())
print(nome.split()[1])
print(nome[0:7])
print(nome.split()[0], len(nome))
print(len(teste))
print(teste[0])

print(type(teste))
print(dir(teste))
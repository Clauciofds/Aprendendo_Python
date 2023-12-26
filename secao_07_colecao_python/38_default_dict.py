'''
Módulo Collection - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido, Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuido.

OBS: Lambdas são funcões sem nome, que podem ou não receber parâmentros de entrada e reornar valores.

'''

dicionario = {'curso': 'Programacao em Python Essecnial'}

print(dicionario['curso'])

# print(dicionario['outro']) # ???? KeyError

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # keyError no dicionario comum, mas aqui nao.

print(dicionario)

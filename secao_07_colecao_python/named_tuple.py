'''
Módulo Collections - Named tuple

São tupla com parâmetro nomeado
'''

from collections import namedtuple

# FORMA I
cachorro = namedtuple('cachorro', 'idade raca nome')

# FORM II
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# FORMA III
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# USANDO A TAPLE

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
ray + cachorro(idade=4, raca='Salcicha', nome='Duda')

print(ray)

# ACESSANDO OS DADOS DA TUPLE
# FORMA I
print(ray[0])
print(ray[1])
print(ray[2])

print('')

# FORMA II
print(ray.idade,
      ray.raca,
      ray.nome)

print(ray.raca)
print(ray.nome)

print('')
print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
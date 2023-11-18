"""
Filter

filter() -> Filtra dados de um coleção de um banco.


"""
from statistics import mean as mda

# Dados Coletados de algum sensor
dados = [1.3, 2.7, 0.8,4.1, 4.3, -0.1]

# Calculando a média
media = mda(dados)

# Obs: Assim como a função map(), a filter() recebe dois parâmetroe, sendo
# uma função e uma variável.

res = filter(lambda x: x > media, dados)
# res = list(res)
res1 = list(filter(lambda x: x > mda(dados), dados))

print(mda(dados))

print(list(res))
print(res1)
print(list(res))
print(list(res1))

# Exemplo 01

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print('')
print(paises)

# forma mais simples
res = filter(None, paises)
print(list(res))

# Formas opcionais:
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))

# Exemplo 02

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carls", "tweets": ["Eu gosto de gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu adoro de cachorros", "Eu adoro pizzas"]},
    {"username": "doggo", "tweets": ["Eu adoro bolos", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usaáurios que estão inativos no X
# Forma 01
inativo = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(f'\n{inativo}')

# Forma 02
inativo = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(f'\n{inativo}')


# Combinardo fitler() e map().

nomes = ['Vanessa', 'Ana', 'Maria']

# Criar uma lista contendo 'Sua instrutora é' + nome, desde que o nome tenha menos de 5 caractes

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(f'\n{lista}')
'''
Mapas -> Conhecidos em Python como Dicionários

Representados por {}
'''

receita = {'jan': 100, 'fev':250, 'mar':400}

print(receita)

# interar sobre dicionarios
for chave in receita:
    print(chave)

print('')

for chave in receita:
    print(receita[chave])

print('')

for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}')

print('')

# Acessando as chaves
print(receita.keys())

print('')

for chave in receita.keys():
    print(receita[chave], chave)

print('')

# Acessano os valores
print(receita.values())

for valor in receita.values():
    print(valor)

print('')

# Desempacontando dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e Valor = {valor}')

print('')

# Soma, Valor Maximo, minino e Tamanho
# Com valores reais

print(sum(receita.values()))
print(max(receita.values()))
print(len(receita))
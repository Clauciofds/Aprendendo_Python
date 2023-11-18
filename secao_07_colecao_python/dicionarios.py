'''
OBS? Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleçoes do tipo chave/valor.

O dicionário são repesentadas por chaves {}.

'''

# FORMA 1
# Forma mais comum de criar dicionarios
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# FORMA 2
paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises1)

print('')

# Acessando elmentos
# FORMA 1 = Acessando via chaves:
print(paises['br'])
# print(paises['ru'])

# FORMA 2
print(paises.get('br'))
print(paises.get('ru'))

print('')

numero = None
print(type(numero))
print(numero)

numero = 1.2, 1.3, 1.4, 1.5,
print(type(numero))
print(numero)
# print(numero.get(1))

print('')

pais = paises.get('ru', 'nao encontrado')

print(f'Encontrado {pais}')

'''
if pais:
    print(f'Encontrie o pais {pais}')
else:
    print(f'Nao encontrie o pais')
'''

print('')

# A Busca em dicionários sempre é feita pelas chaves.
print('br' in paises)
print('ru' in paises)
print('Brasil' in paises)

print('')

localidades = {
    (34.323, 90.345): 'Tokio',
    (12.898, 10.459): 'Sao Paulo',
    (56.940, 56.340): 'Piracicaba'
}

print(localidades)
print(type(localidades))

print('')
# 1 - Podemos utilizar uma Lista.

carrinho = []

produto1 = ['Play Station 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print(type(carrinho))

print('')
# 2 - Podemos usar tuplas.

produto1 = ('Play Satation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)
print(type(carrinho))

print('')
# 3 = Usando dicionários

carrinho = []
subtotal = 0
total = 0

produto1 = {'nome': 'Play Station 4', 'quant': 2, 'preco': 2300.00}
produto2 = {'nome': 'God of War', 'quant': 3, 'preco': 140.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

print('')
print(28 * " -")
print("|     Item             |   Quantidade  |     Subtotal  |")

for produto in carrinho:
    subtotal = produto['quant'] * produto['preco']
    print(f"| {produto['nome']:<20} | {produto['quant']:^13} | R$ {subtotal:>10.2f} |")
    total += subtotal

print(f"| {'Total:':<36} | R$ {total:>10.2f} |")
print(28 * " -")

print('')

d = dict(a=1, b=2, c=3)
print(d)

dic = d.copy()
print(dic)

dic['d'] = 4
print(dic)

# Forma n'ao usual de criação de dicionários

dic = {}.fromkeys('a', 'b')
print(dic)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(11), 'novo')
print(veja)
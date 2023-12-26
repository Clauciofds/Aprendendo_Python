"""
Len, Abs, Sum, Round

-> len() - Retorna o tamanho de um iterável.

"""
# Função len()
print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3}))

print(len(range(1, 10)))

# Função abaixo e denomimada Dunder len
print('Claucio'.__len__())

# Função abs()
print('')
# Exemplo
print(abs(-5))
print(abs(5))
print(abs(-3.14))

# Função sum()
print('')
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 1.5))
print(sum({1, 3, 4, 5}))
print(sum((1, 2, 3, 4, 5)))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))

# Função round()
print('')
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(3.143452, 2))
print(round(1.2199999, 2))
print(round(1.21222222, 2))
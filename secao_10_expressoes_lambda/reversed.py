"""
Reversed

OBS: Não confunda com a função reverse().

A função reverse() só funciona com as listas.

Já a funçao reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

"""

# Exemplo
lista = [1, 2, 3, 4, 5, 6]

res = reversed(lista)
print(type(res))

# Podemos converter o elemento retornado para um Lista, Tupla ou Conjunto

# Lista
print(f'Lista: {list(reversed(lista))}')

# Tupla
print(f'\nTupla: {tuple(reversed(lista))}')

# Conjunto (Set) -- OBS: Em conjunto não definimos a ordem dos elementos
print(f'\nSet: {set(reversed(lista))}')

# Podemos iterar sobre o resersed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem for
print(f"\n\n{''.join(list(reversed('Geek University')))}")

# Podemos fazer mais fácil com slice de strings
print(f"\n{'Geek University'[::-1]}")

# Podemos também utilizar o reversed() para fazer um loop for reverso
print('\n')
for n in reversed(range(0, 10)):
    print(n, end=' ')

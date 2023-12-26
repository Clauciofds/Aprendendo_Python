"""
Any e All

all() -> Retorna True se todos os elementos do iterãove são verdadeiros ou ainda se o iterãvel esta vazio.
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False pelo zero estar contido na lista

print(all([]))
print(all([1, 2, 3, 4]))
print(all('Geek'))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Kassio']

print(f"\n{all([nome[0] == 'C' for nome in nomes])}")

print(all([letra for letra in 'g' if letra in 'aeiou']))
#OBS: Um interável vazio convertido em boolena é False, mas o all() entende um dicionário ou conjunto vazio com True

print(all([num for num in [4,2, 10, 6, 8] if num % 2 == 0]))

# any -> Retorna True se qualquer elemento do iterável forverdadeiro. Se o iterável esgtiver, vazio, retorna False

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

print(any([nome[0] == 'C' for nome in nomes]))
# True mesmo que Kassio esteja no dicionário da vairável nomes any() considera pelo menos um True e retorna True

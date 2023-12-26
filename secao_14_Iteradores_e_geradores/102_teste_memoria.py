"""
Teste de utilização de memória com Generators

# A função gera uma lista utilizando 49%, 1.651MB de memória.
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

gen = fib_lista(20500)  # Desta forma se gera um a lista

# print(gen)

for _ in gen:
    print(_, end=" ")

"""


# Generator usou 14% e 1.601MB de memória
def fib_gen(max):
    a, b, _ = 0, 1, 0
    while _ < max:
        a, b = b, a + b
        yield a
        _ += 1

for n in fib_gen(20):
    print(n, end=' ')
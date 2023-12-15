"""
Teste de Velocidade com Genarators

# Generators (Geradores)
def nums():
    for num in range(1, 10):
        yield num

gen = nums()

print(gen)

print(next(gen))
print(next(gen))


# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)

print(next(ge2))
print(next(ge2))

"""
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))  # 100 milhões
gen_fim = time.time() - gen_inicio


# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(1, 100000000)]))  # 100 milhões
list_fim = time.time() - list_inicio

print(f"Generator Expression = {gen_fim:.2f}s\n"
      f"List Comprehesion = {list_fim:.2f}s")

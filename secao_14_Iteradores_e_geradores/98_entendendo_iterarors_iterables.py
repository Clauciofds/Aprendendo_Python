"""
iterator ->
    -- Um objeto iteravél.
    -- Um objeto que retorna um dado, sendo em elemento por vez quando um função next() é chamado;

Iterable ->
    -- Um objeto que irá retornar um iterator quando a função iter() for chamada.


"""

nome = "Clauc" # É um iterable mas não é um iterator.

numeros = [1, 2, 3, 4, 5, 6] # É um iterable mas não é um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))

res = []

for letra in it1:
    # res.append(letra)
    print(letra, end=" ")

# print(res)
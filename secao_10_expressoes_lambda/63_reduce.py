"""
Reduce

A partir do Python3+ a função reduce() não é mais um função integrada (build-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce(0 se você realmente precisar dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem um coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma funçao que recebe dois parâmetros:

def função(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetro: a função e o iterável.

reduce(função, dados)

A função reduce(), funcionaa da seguinte forma:
    Passo 1: res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do pass1 mais o terceiro elemento e
    guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:
função(função(função(a1, a2), a3), a4), ...), an)

"""

# Como funciona na pratica?

# Vamos utilizar a função reduce() para multiplicar todos os números de um lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30, 50, 100]

# Para utilizar o reduce() nós precimos de uma função que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Fazer o mesmo com loop for

res = 1

for n in dados:
    res *= n

print(f'\n{res}')
"""
Geradores

--> Geradores (generators) são Iterators (Iteradores);

Obs.: O contrário não é verdadeiro.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

______________________________________________________________________________________
)      Funções                         )              Generator Functions            (
) utilizam return                      ( utilizam yield                              (
) retorna uma vez                      ) podem utilizar yield múltiplas vezes        (
) quando executada, retorna um valor   ( quando executada, retorna um generator      (

# OBS: Uma Generator Function não é um Generator. Ela gera um Generator.

gen = conta_ate(5)

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



"""

from colorama import Fore
import string  # Importar string para gerar o alfabéto
s

# EXEMPLO:
# Uma Generator Function não é um Generator. Ela gera um generator.
def conta_ate(valor_maximo):
    _ = 0
    while _ <= valor_maximo:
        yield _
        _ += 1

gen = list(conta_ate(6))

print(gen)

print("Claucio")

for num in gen:
    print(num, end=' ')

print(f"\n{Fore.LIGHTBLUE_EX}")

def alfabeto(valor_maximo):
    _ = 'a'  #Letra inicial do alfabeto
    while _ <= valor_maximo:
        yield _
        _ = chr(ord(_) + 1)

gen = list(alfabeto('f'))

print(gen)

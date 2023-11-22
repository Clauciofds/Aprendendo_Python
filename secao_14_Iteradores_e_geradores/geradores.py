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

# EXEMPLO:
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(10)

for num in gen:
    print(num)
    
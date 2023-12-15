"""
Decorators com diferentes assinaturas

-- Quando a funcao não contém todos os requisistos necessários para funcionamento temos que usar um padrão chamado
Decorator Pattern

"""
from colorama import Fore

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Ola, eu sou a(o) {nome}'


@gritar
def ordenar(principal, acompanhamento, sobremesa):
    return (f'Ola, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'
            f'\nE sobremesa gostaria de {sobremesa}')


# TESTANDO
print(saudacao('Angelina'))


print(Fore.LIGHTCYAN_EX)
print(ordenar('Picanha', 'Batata Frita', 'Torta'))


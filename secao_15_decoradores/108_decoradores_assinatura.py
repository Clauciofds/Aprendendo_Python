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


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento deve ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(Fore.LIGHTWHITE_EX)
# TESTANDO
print(soma_dez(10, 12))

print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))

print(Fore.LIGHTCYAN_EX)
print(comida_favorita('sanduiche', 'pizza'))


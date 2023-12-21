"""
Forçanco tipos de dados com decoradores




num_int = 10
num_float = 10.2
stri = "claucio"

print(type(num_int), type(num_float), type(stri))
"""
from colorama import Fore


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)

        return converte

    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


print(repete_msg('Claucio', '3'))


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


print(Fore.LIGHTCYAN_EX)
dividir('1', 5)

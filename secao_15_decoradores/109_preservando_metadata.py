"""
Preservando metadados com warps

- METADADO = São dados intrícicos em arquivos

- warps = São funções que envolvem elementos com diversas finalidades.


"""
from colorama import Fore
from functools import wraps


# PROBLEMA
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Funcao para verificar o status do usuário no sisitema"""
        print(f'Você está chamado {funcao.__name__}')
        print(f'Aqui a documentocao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b





# SOLUCAO
def ver_log_solucao(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Funcao para verificar o status do usuário no sisitema"""
        print(f'Você está chamado {funcao.__name__}')
        print(f'Aqui a documentocao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log_solucao
def soma_solu(a, b):
    """Soma dois números"""
    return a + b

print(soma_solu.__name__)
print(soma_solu.__doc__)
print(help(soma_solu))
print(ver_log_solucao.__doc__)

# print(soma(10, 30))



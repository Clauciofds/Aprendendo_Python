"""
POO - Abstraçõa e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando

Não se deve fazer esse tipo de acesso a elementos privado de um classe, mas há uma forma de fazer isso:

-> instancia._Pessoa__nome

-> instancia._Pessoa__falar()


- Abstração, em POO, é o ato de expor apenas dados relevantes de um classe, escondendo atributos e métodos
  privados de usuário

"""
from colorama import Fore
print(f'{Fore.RESET}01')

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo: {self.__saldo} do Titular: {self.__titular} com limite: {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


# TESTANDO

conta1 = Conta('Claucio', 1500.50, 1500)

# Como os atributos estão públicos podemos lê-los e alterá-los livremente. Em alguns casos isso causará problemas
# print(
#     f'{conta1.numero}\n'
#     f'{conta1.titular}\n'
#     f'{conta1.saldo}\n'
#     f'{conta1.limite}\n'
# )

# Já com atributos privados, o python não impede de acessá-los, mas é necessário fazê-lo através de seus métodos
# e/ou de forma especiais não recomendadas
print(conta1.__dict__)

conta1.extrato()


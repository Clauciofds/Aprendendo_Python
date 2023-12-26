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
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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
        print(
            f'Saldo: {locale.currency(self.__saldo)} do '
            f'Titular: {self.__titular} com '
            f'limite: {locale.currency(self.__limite)}'
        )

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor incorreto!!!')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!!!')
        else:
            print('Valor incorreto!!!')

    def transferir(self, valor, conta_destino):
        # Sacar da conta de origem
        if valor > 0:
            if self.__saldo > valor:
                self.__saldo -= valor
                self.__saldo -= 10  # Taxa de transferência
            else:
                print('Saldo insuficiente!!!!')
        else:
            print('Valor incorreto!!!')

        # depositar conta destino
        conta_destino.__saldo += valor

# TESTANDO

conta1 = Conta('Claucio', 15000.50, 3000)
conta2 = Conta('Vicente', 20000, 5000)
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

print(f'\n{Fore.LIGHTBLUE_EX}02')
conta1.depositar(1500)

conta1.extrato()

print(f'\n{Fore.LIGHTWHITE_EX}03')

conta1.sacar(10000)

conta1.extrato()

print(f'\n{Fore.LIGHTBLUE_EX}04')

conta1.extrato()
conta2.extrato()
conta1.transferir(5000, conta2)

print('')
conta1.extrato()
conta2.extrato()

print(f'\n{Fore.LIGHTWHITE_EX}05')

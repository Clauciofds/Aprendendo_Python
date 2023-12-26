"""
POO - Objetos

-> São instância da classe, ou seja, após o mapeamento do objeto do mundo real para sua representação computacional,
   devemos poder criar quantos objetos forem necessários. Podemos pensar no objetos/instâncias de uma classe como
   variáveis do tipo difinido na classe.
"""
from colorama import Fore
print(f'{Fore.RESET}01')

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return  self.__ligada

    def ligar_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é: {self.__cliente._Cliente__nome}')


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz_oi(self):
        print(f'O cliente {self.__nome} diz oi!')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos:
lamp1 = Lampada('Azul', 110, 60)

lamp1.ligar_desliga()  # Liga a lâmpada
lamp1.ligar_desliga()  # Desliga a lâmpada

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

# cc1 = ContaCorrente('Claucio', 1000)

user1 = Usuario('Vicente', 'Rodrigues', 'vicente@gmail.com', 1234)

cliente1 = Cliente('Cleiton', '183,456,987-55')

cc2 = ContaCorrente(5000, 1000, cliente1)

print(f'\n{Fore.LIGHTRED_EX}02')

print(cc2.mostra_cliente())



print(f'\n{Fore.LIGHTWHITE_EX}02')
cc2.mostra_cliente()

cc2._ContaCorrente__Cliente.diz()

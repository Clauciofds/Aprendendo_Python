"""
POO - Métodos

- Métodos (funções) -> Representa os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de Classe

--- Método dunder init __init__ é um método especial chamddo construtor e
    sua função é construir o objeto a parti da classe.

OBS.: Todos elementos em python que inicia e finaliza com duplo underline é chamado
      de dunder (Double Underline)

      Os métodos/funções dunder em python são chamado de métodos mágicos.
"""
from colorama import Fore
from passlib.hash import pbkdf2_sha256 as crvp


class Lampada:

    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem):
        """Retorna o valor do produto dom o desconto"""
        return (self.__valor * (100 - porcetagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistme.')

    @staticmethod
    def defincao():
        return 'UXRKE'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crvp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if crvp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]



p1 = Produto('PS4', 'VG', 2300)

print(f'\nR$ {p1.desconto(50):6.2f}')

print(f'\n{Fore.LIGHTCYAN_EX}01')

user1 = Usuario('Claucio', 'Santos', 'clauciofds@gmail.com', '12344')
user2 = Usuario('Cleiton', 'Santos', 'cleito@gmail.com', '432412')

print(user1.nome_completo())
print(user2.nome_completo())
print(user2._Usuario__email)

print(f'\n{Fore.LIGHTWHITE_EX}02')

"""
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
email = input('Email: ')
senha = input('Senha: ')
confirma = input('Confirme senha: ')

if senha == confirma:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha incorret')
    exit (code=1)

print('Usuario criado com sucesso!')

senha = input('Senha: ')

if user.checa_senha(senha):
    print('Acesso permitido.')
else:
    print('Acesso negado!!!')

print(f'Senha User Criptograda: {user._Usuario__senha}')  # Acesso incorreto
"""

# Métodos de Classe


user3 = Usuario('Felicity' , 'Jones', 'felicity@hotmail.com', '1234')

Usuario.conta_usuario()  # Forma correta
# user3.conta_usuario()  # Possi, mas não correto

print(f'\n{Fore.LIGHTCYAN_EX}03')

user4 = Usuario('Claucio', 'Santos', 'claucio@gmail.com', '1234')

print(user4._Usuario__gera_usuario())  # Acesso, de forme errada, não utilize


print(f'\n{Fore.WHITE}04')

# Métodos Estático

print(Usuario.contador)
print(Usuario.defincao())

user5 = Usuario('Vicente', 'Santos', 'vicente@gmail.com', ' 1234')

print(user5.contador)
print(user5.defincao())

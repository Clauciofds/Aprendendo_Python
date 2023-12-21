"""
POO = Atributos

- Atributos = Representa ascaracterísticas do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionamente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    1 - Atributo de Instância;
    2 - " de Classe;
    3 - " Dinâmicos.

1 - Atributos de instâncias: São atributos declarados dentro do método construtor.
    - self = É usado obedecendo uma convençaão, mas pode-se utilizar qualque palavra.


"""
from colorama import Fore

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = f'R$ {(valor * Produto.imposto):6.2f}'
        Produto.contador = self.id


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Cervejaria:

    def __init__(cerveja, nome, amargor, espuma):  # Fora da convenção deve usar o padrão self.
        cerveja.nome = nome
        cerveja.amargor = amargor
        cerveja.espuma = espuma

# Atributos Públicos e Privados:

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Acesso('user@gmail.com', '3452')

print(user.email)

# print(user.__senha)

print(f'{Fore.LIGHTCYAN_EX}01')
user.mostra_senha()
user.mostra_email()

print(f'02{Fore.LIGHTWHITE_EX}\n')
user1 = Acesso('user1@hotmail.com', '2345')

user1.mostra_email()
user1.mostra_senha()

print(f'{Fore.LIGHTCYAN_EX}\n03')

"""
Atributos de Classe são declarados diretamente na classe, ou seja, fora do construtor.
geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja
ao invés de cada instância da classe ter seus próprios valores como é o casa dos atributos de instância, como os
atributos de classe todas as instâncias terão o mesmo valor para este atributo.
"""

p1 = Produto('PS5', 'VG', 3000)
p2 = Produto('Xbox', 'VG', 2900)

print(p1.valor)
print(p2.valor)
print(p1.imposto)  # Acesso possível, mas incorreto de um atributo de classe

print(Produto.imposto)  # Acesso correto do atributo de classe

print(f'{Fore.LIGHTWHITE_EX}\n04')
print(f'{p1.id} - {p1.nome}\n'
      f'{p2.id} - {p2.nome}', end='\n')

"""
OBS.: Em linguagens como o Java, os atributos conhecidos como atributos de Classe aqui em Python
      são chamados de atributos estáticos;
"""

print(f'{Fore.LIGHTCYAN_EX}\n05')
# Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução
# OBS.: O atributo dinâmico será exclusivo da instância que o criou.

p3 = Produto('PS5', 'VG', 3200)
p4 = Produto('Arroz', 'Mercearia', 1.54)

# Criando um atributo em tempo de execução
p4.peso = '5 kg' # Note que na classe Produto não existe o atributo peso

print(f'id: {p4.id}\nProduto: {p4.nome}\nDescricao: {p4.descricao}\nValor: {p4.valor}, Peso: {p4.peso}')

# print(f'Produto: {p3.nome}, Descricao: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

print(f'{Fore.LIGHTWHITE_EX}\n06')

# Deletando atributos de forma dinâmica

print(p1.__dict__)
print(p4.__dict__)

print(f'{Fore.LIGHTCYAN_EX}\n07')
del p4.peso

print(p1.__dict__)
print(p4.__dict__)

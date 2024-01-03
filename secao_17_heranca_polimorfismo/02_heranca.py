"""
POO - Herança (Inheritance)

    A ideia de herança é a reutilização de código e externder a utilização da nossa classe.

    OBS.: Nos podemos utililizar para outras classe os atributos de um métods já cliado.

Cliente:
  - nome;
  - sobrenome;
  - cpf;
  - renda.

Funcionário:
  - nome;
  - sobrenome;
  - cpf;
  - matricula.

Pergunta a se fazer para determinar heranças:
    Existe alguma entidade genérica o suficiente para encapsular os atributos
    e métodos comuns a outras entidades?

- Quando uma classe herda à outra classe ela herda TODOS os atributos e métodos da classe mãe.

    Quando uma classe herda para outra, a classe é chamada por:
    - Super Classe;
    - Classe Mãe;
    - Classe Base;
    - Classe Genérica.

    Quando uma classe herda de outra, ela é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica.

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas.
"""
from colorama import Fore



class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'




class Cadastro:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class ClienteR(Cadastro):
    """Cliente herda de Cadastro"""
    def __init__(self, nome, sobrenonme, cpf, renda):
        super().__init__(nome, sobrenonme, cpf)
        self.__renda = renda


class FuncionarioR(Cadastro):
    """Cliente herda de Cadastro"""
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        # Sobrescrita de Métodos (overriding)
        print(super().nome_completo())
        print(self._Cadastro__cpf)
        return f'Funcionário: {self.__matricula} - Nome: {self._Cadastro__nome}'


def main():
    cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
    funcio1 = Funcionario('Claucio', 'Santos', '987.654.321-00', 23456)

    print(Fore.GREEN)
    print(cliente1.nome_completo())
    print(funcio1.nome_completo())

    cliente2 = ClienteR('Claucio', 'Santos', '321.654.984-00', 10000)
    funcio2 = FuncionarioR('Cleiton', 'Santos', '654.987.123-00', 23123)

    print(Fore.CYAN)
    print(cliente2.nome_completo())
    print(funcio2.nome_completo())
    print(cliente2.__dict__)



    print(Fore.RESET)


if __name__ == '__main__':
    main()

"""
POO - Herança multipla

    Herança Múltipla nada mais é do que a possibilidade de um classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.
  - Por Multiderivaçao Direta;
  - por Multiderivação Indireta.

# EXEMPLO 01 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Multiderivada(Base1, Base2):
    pass

# EXEMPLO 02 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerevacao(Base3):
    pass



"""
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return  f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andanda.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Terrestre, Aquatico):  # A ordem de herança altera a execução dos métodos herdados.
    def __init__(self, nome):
        super().__init__(nome)


# EXECUÇÃO
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

katsu = Pinguim('Katsu')
print(katsu.andar())
print(katsu.nadar())
print(katsu.cumprimentar())  # Method Resolution Order - MRO.

# Objeto é instância de ...

print(f'Katsu é instância de Pinguim? {isinstance(katsu, Pinguim)}')
print(f'Katsu é instância de Aquatico? {isinstance(katsu, Aquatico)}')
print(f'Katsu é instância de Terrestre? {isinstance(katsu, Terrestre)}')
print(f'Katsu é instância de Animal? {isinstance(katsu, Animal)}')
print(f'Katsu é instância de object? {isinstance(katsu, object)}')
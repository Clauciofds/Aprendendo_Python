"""
POO - MRO - Method Resolution Order


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


class Pinguim(Aquatico, Terrestre):  # A ordem de herança altera a execução dos métodos herdados.
    def __init__(self, nome):
        super().__init__(nome)


# EXECUÇÃO
katsu = Pinguim('Katsu')

print(katsu.cumprimentar())  # Method Resolution Order - MRO.

"""
- Código:
Pinguim(Terrestre, Aquatico)
- Saída:
Eu sou Katsu da terra

- Código:
Pinguim(Aquatico, Terrestre)
- Saída:
Eu sou Katsu da mar
"""
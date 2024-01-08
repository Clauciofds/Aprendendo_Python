"""
POO - Polimorfismo

Poli - Muitas
Morfis - Formas


"""

class Animal(object):
    def __init__(self, nome, genero):
        self.__nome = nome
        self.__genero = genero

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome, genero):
        super().__init__(nome, genero)

    def falar(self):
        print(f'{self._Animal__nome} fala wauwau')


class Gato(Animal):
    def __init__(self, nome, genero):
        super().__init__(nome, genero)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):
    def __init__(self, nome, genero):
        super().__init__(nome, genero)

    def falar(self):
        print(f'{self._Animal__nome} fala gich gich')


# EXECUÇÃO
felix = Gato('Felix', 'macho')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto', 'macho')
pluto.comer()
pluto.falar()

mickey = Rato('Minne', 'femea')
mickey.comer()
mickey.falar()
"""
POO - O método supe()

O método super() se refere à super classe.


"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # Desta forma é possivel acessar o método mãe (não recomendado)
        super().__init__(nome, especie)  # Recomendado
        super().faz_som('auau')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')
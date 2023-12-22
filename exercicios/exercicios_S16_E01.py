"""
Crie uma classe para representar uma pessoa, com os atributos privados
de nome, idade e altura. Crie os métodos públicos necessários para
sets e gets e também um método para imprimir os dados de uma pessoa.
"""


class Peopple:
    """This class define and modified names, age and heigth of peapple."""
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__heigth = height

    #  Method with getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_heigth(self):
        return self.__heigth

    # Method with setters new attributes
    def set_new_name(self, name):
        self.__name = name

    def set_new_age(self, age):
        self.__age = age

    def set_new_heigth(self, heigth):
        self.__heigth = heigth

    # Print All Object Attributes
    def print_data(self):
        print(
            f'Name: {self.__name}\n'
            f'Age: {self.__age}\n'
            f'Heigth: {self.__heigth}'
        )


p1 = Peopple('Claucio', 50, 1.73)

p1.print_data()

p1.set_new_heigth(1.70)

p1.print_data()

print(p1.get_heigth())

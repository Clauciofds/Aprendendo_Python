from colorama import Fore


class Motorcycle:
    """
     1ª ETAPA
     Escreva um código em Java que apresente a classe Moto, com atributos marca,
     modelo, cor e marcha e, o método imprimir. O método imprimir deve mostrar na
     tela os valores de todos os atributos. O atributo marcha indica em que a
     marcha a moto se encontra no momento, sendo representado de forma inteira,
     onde 0 - neutro, 1 - primeira, 2 - segunda, etc.

     Construa um método construtor que permita a definição de todos os atributos
     no momento da instanciação do objeto.

     2ª ETAPA
     Inclua os métodos marchaAcima e marchaAbaixo que deverá efetuar a troca de marchas
     onde, os métodos deverão deverão fazer uma troca de cada vez para cima ou para baixo,
     verificando se as marchas estão no minímo Neutro ou na mais alto, sexta marcha. E os
     métodos dever imprimir em que marcha a moto está engatada.
    """

    def __init__(self,manufacturer, model, predominant_color, gear):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__predominant_color = predominant_color
        self.__gear = gear

    # 2ª ETAPA
    def get_gears(self):
        # Creating a six-speed gearbox
        gears = ['Neutral', 'First gear', 'Second gear', 'Third gear', 'Fourth gear', 'Fifth gear', 'Sixth gear']
        return gears

    @property
    def set_gear(self):
        return self.__gear

    @set_gear.setter
    def set_gear (self, new_value):
        if new_value == 1:
            if 0 <= self.__gear < 6:
                self.__gear += 1
                print(f'\nGear engaged: {Fore.GREEN}{self.get_gears()[self.__gear]}{Fore.RESET}')
            else:
                print(f'\n{Fore.LIGHTGREEN_EX}Sixth gear engaged!!!{Fore.RESET}')
        else:
            if 6 >= self.__gear > 0:
                self.__gear -= 1
                print(f'\nGear engaged: {Fore.RED}{self.get_gears()[self.__gear]}{Fore.RESET}')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Neutral gearbox{Fore.RESET}')

    def view_info(self, gears=None):
        # Creating a six-speed gearbox
        gears = ['Neutral', 'First gear', 'Second gear', 'Third gear', 'Fourth gear', 'Fifth gear', 'Sixth gear']

        print(f'{4*"*"}  Your Motorcycle  {4*"*"}\n')
        print(
            f'Manufacturer: {self.__manufacturer}\n'
            f'Model: {self.__model}\n'
            f'Predominant color: {self.__predominant_color}\n'
            f'Gear engaged: {gears[self.__gear]}'
        )


def main():
    print('\n--Enter purchase Order--')
    manufacture = input('Manufacturer: ')
    model = input('Model: ')
    predominant_color = input('Predominante color; ')

    purchase_order = Motorcycle(manufacture, model, predominant_color, gear=0)
    print('\n* Motorcycle Bill of Sale *')
    purchase_order.view_info()

    while True:
        try:
            change_gear = int(input(
                '\nChange gear...\n'
                '0 for down gear.\n'
                '1 for up gear.\n'
                '...: '
            )
            )

            if change_gear == 0:
                purchase_order.set_gear = change_gear
                contin = input(
                    'Will it continue (Y/N) ?'
                ).lower()
                if contin == 'n':
                    break
            elif change_gear == 1:
                purchase_order.set_gear = change_gear
                contin = input(
                    'Will it continue (Y/N) ?'
                ).lower()
                if contin == 'n':
                    break
            else:
                print(f'\n{Fore.LIGHTBLUE_EX}Pull the clutch!!!`{Fore.RESET}')
        except ValueError as err:
            print(f'Pull the clutch!!! {err}')


if __name__ == '__main__':
    main()

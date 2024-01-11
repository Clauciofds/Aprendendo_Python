class Equipment:
    """
    01 STAGE
    Crie um novo pacote com o nome: exercicios_S17_2_E01_heranca. Todas as 03
    classes criadas deverão ser salvas neste pacote.
    """
    def __init__(self, manufacture, model):
        """
        Criar uma classe Equipamento com 02 atributos privados.
        :param manufacture: str
        :param model: str
        """
        self.__manufacture = manufacture
        self.__model = model

    def get_manufature(self):
        return self.__manufacture

    def get_model(self):
        return self.__model

    def shopping_list(self):
        shopping_list = [self.__manufacture, self.__model]
        return shopping_list

    def check_shopping_list(self):
        print('\n* Equipment check list *')
        print(
            f'{"Manufacture:":.<14}{self.__manufacture}\n'
            f'{"Model:":.<14}{self.__model}\n'
       )


class Computer(Equipment):
    def __init__(self, manufacture, model, ssd_cap, mem_cap):
        """
        Criar uma Classe Computaodor com dois atributos à sua escolha, também privados.
        A classe Computador deverá herdar tudo da classe Equipamento.
        :param manufacture: str (herança de Equipqmento)
        :param model: str (heranção de Equipamento)
        :param ssd_cap: int - Capacidade de armazenamento do SSD
        :param mem_cap: int - Capacidade de armazenamento da memória RAM

        02 STAGE
        Criar os métodos de acesso e de modificação para os atributos definidos em ambas
        as classes.

        """
        super().__init__(manufacture, model)
        self.__ssd_cap = ssd_cap
        self.__mem_cap = mem_cap

    def shopping_list(self):
        shopping_list = super().shopping_list() + [self.__ssd_cap, self.__mem_cap]
        return shopping_list

    def check_shopping_list(self):
        print('\n* Computer check list *')
        print(
            f'{"Manufacture:":.<14}{self.shopping_list()[0]}\n'
            f'{"Model:":.<14}{self.shopping_list()[1]}\n'
            f'{"SSD:":.<14}{self.shopping_list()[2]}GB\n'
            f'{"RAM:":.<14}{self.shopping_list()[3]}GB'
        )

    # 02 STAGE
    @property
    def modify_shop_list(self):
        return self.shopping_list()

    @modify_shop_list.setter
    def modify_shop_list(self, values):
        new_manufacture, new_model, new_ssd_cap, new_mem_cap = values
        self._Equipament__manufacture = new_manufacture
        self._Equipament__model = new_model
        self.__ssd_cap = new_ssd_cap
        self.__mem_cap = new_mem_cap

        new_shopping_list = self._Equipament__manufacture, self._Equipament__model, self.__ssd_cap, self.__mem_cap
        return new_shopping_list


class TestEquipment(Equipment, Computer):
    @staticmethod
    def main():

        bill_list_01 = Equipment('Positivo', 'Serie XX')
        bill_list_01.check_shopping_list()

        bill_list = Computer('HP', '55S', 120, 8)
        bill_list.check_shopping_list()

        print('\n*  Change list  *')
        new_manufacture = input('New manufacture: ')
        new_model = input('New model: ')
        new_ssd_cap = input('New SSD: ')
        new_mem_cap = input('Nem memory: ')

        bill_list.modify_shop_list = new_manufacture, new_model, new_ssd_cap, new_mem_cap

        bill_list.check_shopping_list()

    if __name__ == '__main__':
        main()

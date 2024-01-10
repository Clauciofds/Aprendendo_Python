class Equipament:
    def __init__(self, manufature, model):
        self.__manufature = manufature
        self.__model = model

    def get_manufature(self):
        return self.__manufature

    def get_model(self):
        return self.__model

    def shopping_list(self):
        shopping_list = [self.__manufature, self.__model]
        return shopping_list


class Computer(Equipament):
    def __init__(self, manufature, model, ssd_cap, mem_cap):
        super().__init__(manufature, model)
        self.__ssd_cap = ssd_cap
        self.__mem_cap = mem_cap

    def shopping_list(self):
        shopping_list = super().shopping_list() + [self.__ssd_cap, self.__mem_cap]
        return shopping_list

    def check_shopping_list(self):
        print(self.shopping_list())

def main():
    bill_list = Computer('PH', '55S', 120, 8)
    bill_list.check_shopping_list()

if __name__ == '__main__':
    main()

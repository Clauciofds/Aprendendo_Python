class Rectangle:
    """
    Escreva um código que apresente a classe Retângulo, com atributos comprimento, largura,
    àrea, perímetro e os métodos calcularArea, calcularPedrimetro e imprimir os métodos
    calcularArea e calcularPerimetro devem efeturar seus respectivos cálculos e colocar
    os valores nos atributos área e perimetro. O método imprimir deve mostrar na tela os
    valores de todos os atributo. Salienta-se que a área de um retângulo é obtida pela fórmula:
    > comprimeto * largura; e
    Perimetro:
    > 2 * comprimento + 2 * largura.

    Adicione um método construtor que permita a definição de todos os atributos no momento
    da instanciação do objeto.
    """
    def __init__(self, side, height):
        self.__side = side
        self.__height = height

    def area_calculate (self):
        area = self.__side * self.__height
        return area

    def perimeter_calculate(self):
        perimeter = 2 * self.__side + 2 * self.__height
        return perimeter

    def view_info(self):
        print(
            f'\nRectangle info.\n'
            f'Side: {self.__side}\n'
            f'Height: {self.__height}\n'
            f'Area: {self.area_calculate()}\n'
            f'Perimeter: {self.perimeter_calculate()}'
        )


def main():
    print('* Enter rectangle Dimensions *')
    side1 = float(input('Side: '))
    height1 = float(input('Height: '))

    rect = Rectangle(side1, height1)

    rect.view_info()

if __name__ == '__main__':
    main()
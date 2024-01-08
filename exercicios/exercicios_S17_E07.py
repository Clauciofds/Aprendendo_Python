from math import pi

class Circle:
    """
    Escreva um código que apresente a classe Retângulo, com atribuotos
    comprimento. largura, área, perímetro e os métodos calcularArea,
    colacularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
    devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e
    perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.
    Salienta-se que a área de um circulo é obtida pela fórmula (pi ^ raio) e o perímetro
    por 2 * pi * raio).
    """
    def __init__(self, radius_circle):
        self.__radius_circle = radius_circle

    def area_circle(self):
        area = pi * self.__radius_circle
        return area

    def perimeter_circle(self):
        perimeter = 2 * pi * self.__radius_circle
        return perimeter

    def view_info(self):
        print('\n Circle info\n')
        print(
            'Radius: {:05.2f}\n'.format(self.__radius_circle),
            'Area: {:05.2f}\n'.format(self.area_circle()),
            'Perimeter: {:05.2f}'.format(self.perimeter_circle())
        )


def main():
    print('\n* Enter Radius Circle *')
    while True:
        try:
            radius1 = float(input('Radius: '))
            break
        except ValueError as err:
            print(f'Incorrect!!! {err}')

    circle = Circle(radius1)

    circle.view_info()


if __name__ == '__main__':
    main()
class Quadrado:
    """
    Escreva um código que apresente a clsse Quadrado, com atributos lado, área e perímietro.
    Os métodos calcular área, calcular Perimetro e imprimir.
    Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos cálculos e
    colocar os valores no atributos area e perimetro. O método imprimir deve mostror na tela
    os valores de todos os atributos. Salienta-se que a área de um quadrado é obtida pela
    fórmula (lado * lado) e perímetro por (4 * lado).
    """
    def __init__(self, lado):
        self.__lado = lado

    def perimeter_square(self):
        perimeter = self.__lado * 4
        return perimeter

    def area_square(self):
        area = self.__lado * self.__lado
        return area

    def print_info(self):
        option = int(input(
            '      Menu\n'
            '1 - Square Area.\n'
            '2 - Peremeter Square.\n'
            '3 - Both.\n'
            'Enter option: '
            )
        )

        if option == 1:
            print(
                f'\nSquare side: {self.__lado}\n'
                f'Square area: {self.area_square()} mm²'
            )
        elif option == 2:
            print(
                f'\nSquare side: {self.__lado}'
                f'\nSquare side: {self.__lado}\n'
                f'Perimeter: {self.perimeter_square()}mm'
        )
        else:
            print(
                f'\nArea: {self.area_square()}mm² - Peremeter: {self.perimeter_square()}mm'
            )



def main():
    square_side = int(input('\nEnter square side (mm): \n'))

    square1 = Quadrado(square_side)

    square1.print_info(area=square_side, perimeter=square_side)


if __name__ == '__main__':
    main()

class Apliance:
    """
    17) Escreva um código em Java que apresente a classe Eletrodoméstico, com atributo
    ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de
    todos os atributos. O atributo ligado será boleeano e deverá indicar o estado atual
    do eletrodoméstico, se ligado ou desligado.

    18) Baseando-se no exercício 17 adicione um método construtor que permita a definição
    de todos os atributos no momento da instanciação do objeto.

    19) Baseando-se no exercício 18 adicione os métodos ligar e desligar que deverão
    mudar o conteúdo do atributo ligado conforme o caso.

    """
    def __init__(self):
        self.__turn_on = False

    def view_status(self):
        if self.__turn_on == False:
            current_status = "Turn off"
            print(f"\nAliance is: {current_status}")
        else:
            current_status = "Turn on"
            print(f"\nAliance is: {current_status}")

    @property
    def current_status(self):
        return self.__turn_on

    @current_status.setter
    def current_status(self, key_position):
        if key_position == 1:
            self.__turn_on = True
        else:
            self.__turn_on = False


def main():
    mixer = Apliance()

    mixer.view_status()

    mixer.current_status = 1

    mixer.view_status()


if __name__ == '__main__':
    main()

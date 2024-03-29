from datetime import datetime as dt

class People:
    # Create a Date-Based number serie
    code_id = float(dt.today().strftime('%Y%m%d') + '.00')

    def __init__(self, name, birthday):
        """
               Crie classe Pessao e 03 variáveis de instância:
               :param code: float Criação automática da série id baseada na data para ordenção crescente da criação de novos
                            registros
               :param name: str
               :param birthday: datetime
               """
        print('\n*  Default Builder  *')

        self.__code = People.code_id + 0.01
        self.__name = name
        self.__birthday = dt.strptime(birthday, '%d/%m/%Y')
        People.code_id = self.__code

    def view_info(self, print_birthday=True):
        """
        Crie um método exibe() que receba como parâmetro um número inteiro e decida por meio
        do valor desse parâmentro se a idade será exibida ou não. Para isso use o seguinte
        critério:
        1 para visualizar a idade
        Se não, nãa imprima a idade.
        :return: view info contact
        """

        print(f'{21 * "-"}\n'
              f'*      Contact      *')
        print(
              f'ID: {self.__code:.2f}\n'
              f'Name: {self.__name}'
        )

        if print_birthday:
            print(
                f'Birthday: {self.__birthday.strftime("%d/%m/%Y")}'
            )

    def __str__(self):
        return f'ID: {self.__code}, Name: {self.__name}, Birthday: {self.__birthday.strftime("%d/%m/%Y")}'


class PeopleTest(People):
    def __init__(self, name, birthday):
        """
        Criar uma classe TestPessoa que instancie um objeto da classe Pessoa
        usando o construtor padrão
        :param name: str (herança People)
        :param birthday: datetiem (herança People)
        """
        super().__init__(name, birthday)


def main():
    people1 = People('Claucio', '17/08/1973')

    people1.view_info(print_birthday=True)

    people2 = PeopleTest('Cleiton', '04/04/1982')
    people2.view_info(print_birthday=False)


if __name__ == '__main__':
    main()

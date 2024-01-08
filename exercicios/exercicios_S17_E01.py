class People:
    """
    Escreva um código que apresente a classe Pessoa, com atributo nome,
    endereço e telefone e o método imprimir. O método imprimir deve mostra
    na tela os valores de todos os atrigutos
    """
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def view_info(self):
        return (
            f'\nName: {self.__name}\n'
            f'Address: {self.__address}\n'
            f'Phone: {self.__phone_number}\n'
        )

def main():
    name = input('\nName: ')
    address = input('Address: ')
    phone_number = input('Phone: ')

    contact = People(name, address, phone_number)

    print(contact.view_info())

if __name__ == '__main__':
    main()
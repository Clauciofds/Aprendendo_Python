"""
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as
seguintes operações:

> void armazenaPessoas(String nome, int idade, float altura);
> void removePessoa(String noma);
> int buscaPessoa(String noma);  // informa em que posição da agena está a pessoa;
> void imprimeAgenda();  // imprime os dados de todas as pessoas da agenda
> void imprimePessoa(int index);  // imprime os daods da pessoa que está na posição "i" da agenda.
"""

from colorama import Fore

class Contacts:
    def __init__(self, contact_id, name, age, heigth):
        self.contact_id = contact_id
        self.name = name
        self.age = age
        self.heigth =heigth


class AddressBook:
    def __init__(self):
        self.contacts = []

    def set_contact(self, contact):
        self.contacts.append(contact)

    def print_addres_book(self):
        print(f'{Fore.LIGHTWHITE_EX} ID - {"Name":<20}  - Age - {"Heigth":^3}')
        for contact in self.contacts:
            if int(contact.contact_id) % 2 == 0:
                print(
                    f'{Fore.CYAN} '
                    f'{contact.contact_id:<3} '
                    f'{contact.name:<20}'
                    f'{contact.age}'
                    f'{contact.heigth:>5}'
                )
            else:
                print(
                    f'{Fore.WHITE} '
                    f'{contact.contact_id} '
                    f'{contact.name:<20}'
                    f'{contact.age}'
                    f'{contact.heigth:>5}'
                )


contacts_list = AddressBook()

ab_size = int(input('How many registrations: '))

for i in range(1, ab_size + 1):
    name = input('Name: ')
    age = input('Age: ')
    heigth = input('Heigth: ')

    contact = Contacts(contact_id=i, name=name, age=age, heigth=heigth)

    contacts_list.set_contact(contact)

contacts_list.print_addres_book()
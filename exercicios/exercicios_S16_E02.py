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
    """Create a Planner class that can hold 10 people or less than that and is able to perform the
following operations:

> void stores (String name, int age, float height);
> void remove contact(String noma);
> int search contact(String noma);  # informs what position of the Address book the person is in;
> void print Address book;  # Prints the data of all the people in the address book
> void print Contact(int index);  # Prints the data of the person who is in the "i" position of the address book."""

    def __init__(self, contact_id, name, last_name, age, heigth):
        """Constructs the contact details from the address book
        - ID = int
        - last_name = str
        - name = str
        - age = int
        - heigth = float
        """
        self.contact_id = contact_id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.heigth =heigth

    def full_name(self):  # concatenates the last name with the name
        return f'{self.name} {self.last_name}'


class AddressBook:
    changes_counter = 0  # Class variable to track changes

    def __init__(self):
        """Creates the contact list from the address book"""
        self.contacts = []

    def set_contact(self, contact):
        self.contacts.append(contact)
        self.changes_counter += 1  # Increments the change counter

    def del_contact(self):
        contact_id_to_delete = int(input('\nEnter the ID to delete: '))

        for contact in self.contacts:
            if contact.contact_id == contact_id_to_delete:
                self.contacts.remove(contact)
                print(f'Contact with ID {contact_id_to_delete} deleted.')

        # Creating an Address Book Instance
        self.print_addres_book()
        return

    def get_contact(self):
        search_contact = int(input('Search: '))

        print(f'\n{Fore.LIGHTWHITE_EX} ID - {"Name":<21}  - Age - {"Heigth":^3}')

        for contact in self.contacts:
            if contact.contact_id == search_contact:
                full_name = contact.full_name()
                print(f'{Fore.WHITE}  '
                      f'{contact.contact_id:<4}'
                      f'{full_name:<25}'
                      f'{contact.age:<5}'
                      f'{contact.heigth:>5.2f}{Fore.RESET}')
                break
            else:
                print(f'Contact whit ID {search_contact} not found!!')

    @staticmethod  # Add the decorator to make the method static
    def print_addres_book(self):
        print(f'\n{Fore.LIGHTWHITE_EX} ID - {"Name":<21}  - Age - {"Heigth":^3}')
        for contact in self.contacts:
            if int(contact.contact_id) % 2 == 0:
                full_name = contact.full_name()
                print(
                    f'{Fore.CYAN} '
                    f'{contact.contact_id:<4} '
                    f'{full_name:<25}'
                    f'{contact.age:<5}'
                    f'{contact.heigth:>5.2f}{Fore.RESET}'
                )
            else:
                full_name = contact.full_name()
                print(
                    f'{Fore.WHITE} '
                    f'{contact.contact_id:<4} '
                    f'{full_name:<25}'
                    f'{contact.age:<5}'
                    f'{contact.heigth:>5.2f}{Fore.RESET}'
                )

        return print(f'Total changes: {AddressBook.changes_counter}')

def ad_size():
    contacts_list = AddressBook()

    while True:
        ab_size = int(input('How many registrations: '))

        if ab_size <= 10:
            for i in range(1, ab_size + 1):
                surname = input('\nSurname: ')
                name = input('Name: ')
                age = int(input('Age: '))
                heigth = float(input('Heigth: '))

                contact = Contacts(contact_id=i, name=name, last_name=surname, age=age, heigth=heigth)

                contacts_list.set_contact(contact)

        else:
            print('\nMaximum capacity of the Address book is 10!!\n')

        return contacts_list  # return to Address Book instance
        break


def main():
    # Creates a variable for the address book
    address_book = None

    while True:
        # Create header menu
        print(f"\n{5 * '*'}{'    Menu    '}{5 * '*'}")
        # Create menu to access Address Book
        # Exception raised when a variable is not found in the local or global scope.
        try:
            options_menu = int(input(
                '1 - New contact\n'
                '2 - Delete contact\n'
                '3 - Print address book\n'
                '4 - Search contact\n'
                '\nEnter option: '
            ))

            if options_menu == 1:
                address_book = ad_size()
            elif options_menu == 2:
                address_book.del_contact()
                new_choice = input('\nWould you like to try again (Y/N): ').lower()
                if new_choice == 'n':
                    break
            elif options_menu == 3:
                address_book.print_addres_book(address_book)
            else:
                address_book.get_contact()

        except (ValueError, NameError, TypeError, AttributeError) as err:
            print(err)
            new_choice = input('\nWould you like to try again (Y/N): ').lower()
            if new_choice == 'n':
                break



if __name__ == '__main__':
    main()

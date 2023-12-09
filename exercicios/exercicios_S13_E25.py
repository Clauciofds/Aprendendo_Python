"""
Faça um program gerenciar um agenda de contatos. Para cada contato armazene o nome, o telefone e o
aniversário (dia e mês). O programa deve permitir:

(a) inserir contatos
(b) remover contato
(c) pesquisar um contato pelo nome
(d) listar todos os contatos
(e) listar os contatos cujo nome incia com um letra dade
(f) imprimir os anivesariantes do mês.

Sempre que o programa form encerrado. os contatos deverm ser armazenados em um arquivo binário. Quando o programa
iniciar, os contatos devem ser inicializado com os dados contidos neste arquivo binário.
"""

import os
from datetime import datetime

os.chdir(os.path.join("archives"))

def menu_option():
    print(f'{5 * "*":<10}{"Menu de Contatos":^16}{5 * "*":>10}')

    print(
        "(a) Inserir\n"
        "(b) Remover\n"
        "(c) Pesquisar\n"
        "(d) Listar todos\n"
        "(f) Aniversáriante mês"
    )
    op_option = input("Option: ")

    return op_option


def read_data(contacts):
    # Create an empty list
    contacts = []

    # Read binary file and append in contacts[]
    with open('contatos.bin', 'rb') as file:
        data = file.readlines()
        for i in data:
            line = i.decode("utf-8").split(" - ")
            contacts.append(line)
        contacts = [[item[0], item[1], item[2].strip("\r\n")] for item in contacts]

    return contacts


def insert_contact():
    with open("archives/contatos.bin", "ab") as file:
        # Create empty list
        new_contact = []
        while True:
            # Enter contact details
            name = input("Name: ")
            phone_number = input("Cellphone number: ")

            # Check format Cellphone number with 10 digits
            if len(phone_number) == 11:
                phone_number = f"({phone_number[:2]}) {phone_number[2:7]}-{phone_number[7:]}"
            else:
                print("Incorrect Cellphone number!")

            aniver_data = input("Birthday day and month: ")

            finished = input("More one?\n"
                             "(Y/N): ")

            if finished == "y" and finished == "Y":
                new_contact.append((name, phone_number, aniver_data))
            else:
                new_contact.append((name, phone_number, aniver_data))
                break


def remove_contact(contacts):
    # Enter the contact information that will be removed
    contact_to_remove = input(
       "Contact that will be removed:\n"
       "Name/Cellphone"
    )

    # Remove if existed contact
    while True:
        if contact_to_remove in contacts:
            contacts.remove(contact_to_remove)
            print("Contact removed!")
            break
        else:
            print("Contact not found!")

        # Create and code the new contacts list
        new_contacts = f"{contacts[0]} - {contacts[1]} - {contacts[2]}"
        new_contacts = new_contacts.encode("utf-8")
        with open("contatos.bin", "wb") as file:
            file.write(new_contacts)


def search_contact(contacts):
    # Save contacts list with variably
    list_of_contacts = read_data(contacts)


    while True:
        # Enter info for search
        info_to_search = input("Contact`s info for search: ").lower()

        if len(info_to_search) < 2:
            print("Please enter at least two characters for the search.")
            continue

        # Create empty list to save contact
        found_contacts = []

        # Flag to track if the contact is found
        contact_found = False

        # The loop searches for the item in the sublists of the list.
        for contact in list_of_contacts:
            for item in contact:
                # Restringindo a busca para nomes e DDDs com pelo menos dois caracter
                if len(info_to_search) >= 2 and (item.lower().find(info_to_search) != -1 or contact[1][1:3] == info_to_search):
                    found_contacts.append(contact)
                    contact_found = True  # Flag for contact found and breaks the search so that there are no
                                          # duplicates in the information
                    break

        # If an information is true, the contact will be printed
        if found_contacts:
            print(f"\nContact found: ")
            for contact in found_contacts:
                print(f"Name: {contact[0]} - Phonecell: {contact[1]} - Birthday: {contact[2]}")

            # Option for the new search.
            continue_search = input("\nDo you continue search (Y/N): ")
            if continue_search.lower() != "y":
                break
        # Informations is False:
        else:
            print("\nContact not found!\n")
            continue_search = input("Do you continue search (Y/N): ")

        # Again option for continue search
        if continue_search.lower() != "y":
            break


def main():
    search_contact(contacts="")



if __name__ == "__main__":
    main()





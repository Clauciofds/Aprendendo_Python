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
            line = i.decode("utf-8").contacts.split(" - ")
            contacts.append(line)
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

            if finished == "y" and finished == "Yll":
                new_contact.append((name, phone_number, aniver_data))
            else:
                new_contact.append((name, phone_number, aniver_data))
                break
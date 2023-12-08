from datetime import datetime
import re


def read_data():
    # Create an empty list
    contacts = []

    # Read binary file and append in contacts[]
    with open('archives/contatos.bin', 'rb') as file:
        data = file.readlines()
        for i in data:
            contents_raw = i.decode("utf-8").split(" - ")
            contacts.append(contents_raw)

        # Remove the caracters "\r\n"
        contacts = [[item[0], item[1], item[2].strip("\r\n")] for item in contacts]

    return contacts


def insert_contact():
    name = input("Name: ")
    phone_number = input("Cellphone number: ")
    while open("archives/contatos.bin", "ab") as file:



# Chamar a função
contacts_data = read_data()
print(contacts_data)

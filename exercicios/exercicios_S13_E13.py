"""
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o
número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no
arquivo (ignorando as letras com acento).
Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.

"""
import os

os.chdir(os.path.join("..", "..", "..",".."))
print(os.getcwd())

while True:
    try:
        new_path = input("Current directory:\n"
                     "Or S is read: ")
        if new_path != "s" and new_path != "S":
            os.chdir(os.path.abspath(os.path.join(new_path)))
            print(os.getcwd())
        else:
            break
    except FileNotFoundError as err:
        print(err)
print(f"\n{os.getcwd()}\n")

file_name = input("File name: ")
file_name += ".txt"
new_contact = input("Name: ")
phone_num = input("Phone number: ")

with open(file_name, "a") as archive:
    archive.write(f"\n{new_contact} - {phone_num}")

with open(file_name, "r") as archive:
    print(f"\n{archive.read()}")


"""
Escreva um programa que:
(a) Crie/abra um arquivo de texto de nome "arq.txt
(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário
    entre com o caractere "O"
(c) Feche o arquivo

Agora, abra e leio o arquivo, caractere por caractere, e escreva na tela todos os caracteres e armazenados.
"""

import os

# print(os.getcwd())

with open("archives/exercice_S13_E1.txt", "a") as archive:
    while True:
        word = input("Chose your word or type O for exit.\n"
                     "Type were: ")
        if word != "o" and word != "O":
            archive.write(f"{word}\n")
        else:
            print("")
            break

with open("archives/exercice_S13_E1.txt") as archive:
    print(archive.read())

print(f"The archive is closed?\n"
      f"{archive.closed}")
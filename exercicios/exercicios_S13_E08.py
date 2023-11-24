"""
Faça um programa que leia o conteúndo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras
minúsculas convertidas em maiúsculas. Os nomes dos arquivos serão fornecido, via teclado, pelo usuário. A função que
converte maiúscala para minúsculas é o lower(). Ela é aplicada em cada caractere da string.
"""

import os

# with open("archives/exercice_S13_E1.txt", "r") as archive:
#     new_name = input("New archive name?\n")
#     new_name = new_name + ".txt"
#     with open("archives/exercice_S13_E1.txt", "r") as old_archive:
#         content = old_archive.read()
#
#     with open(os.path.relpath(os.path.join("archives", new_name)), "w") as new_archive:
#         new_content = content.lower()
#         new_archive.write(new_content)

print(os.getcwd())
directory_chose = os.chdir(os.path.join("archives"))

directory = list(os.scandir())
directory_list = []
counter = 1


for i in range(len(directory)):
    print(f"{counter} - {list(os.scandir())[i].name}")
    directory_list.append(i)
    counter += 1

user_chose = int(input("Chose the number of archive for print: "))
# user_chose -= user_chose
print(user_chose)

with open(os.path.relpath(directory[user_chose].name)) as archive:
    print(archive.read())


caminho = os.path.relpath(directory[user_chose].path)
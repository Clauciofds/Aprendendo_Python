"""
Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto
contendo o texto do arquivo de entrada, mas com as vogias substituídas por "*".
"""

with open("archives/exercice_S13_E1.txt", "r") as archive:
    body_list = archive.read()
    vowel = "aeiouAEIOU"
    modified_content = ""
    for char in body_list:
        if char in vowel:
            modified_content += "*"
        else:
            modified_content += char
        with open("archives/new_text.txt", "w") as new_archive:
            new_archive.write(modified_content)

with open("archives/new_text.txt") as archive:
    print(archive.read())


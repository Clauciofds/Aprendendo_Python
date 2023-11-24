"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui.
"""

with open("archives/exercice_S13_E1.txt", "r") as archive:
    print(f"The word list have {len(archive.readlines())} lines")
    


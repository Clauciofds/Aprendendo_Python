"""
Faça um programa que recebe o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada
linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saía onde aparece o nome da cidade mais populosa seguindo pelo número de habitantes.

Minha tabela de cidade brasileiras contém:

No cabeçalho 03 colunas: Cidade, UF, população
No corpo da tabela 50 linhas

"""
# Importando csv que é um bibliotéca que trabalha e reconhece tabelas e planilhas
import os, csv

# User input with the name of the output file
output_archive = input("Name of output file: ")
output_archive += ".txt"

os.chdir(os.path.join("archives"))

# print(os.getcwd())

with open("densidade_demografica.txt", "r") as archive:
    # Read text file as a list of the lists
    data = list(csv.reader(archive, delimiter="\t"))

    # Separete of header of list
    header = data[0]

    # Create a empty dictionary
    dic = {}

    # Interate over the rows in the list
    for row in data[1:]:
        # Get the city name as key
        city = row[0]
        # create a nested dictionary with column values
        values = dict(zip(header[1:], row[1:]))
        # add nested dictionary to main dictionary
        dic[city] = values


    max_population = 0
    max_city = ""

    for key, values in dic.items():
        populations = int(values["population"])
        if populations > max_population:
            max_population = populations
            max_city = key

    with open(output_archive, "w") as new_archiv:
        new_archiv.write(f"A cidade mais populosa é {max_city} com {max_population:,.0f} habitantes")


with open(output_archive, "r") as archive:
    -*- coding: utf-8 -*-
    print(f"\n{archive.read()}")



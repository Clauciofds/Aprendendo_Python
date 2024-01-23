"""
Escrevendo em arquivos csv

Método writer()

-- writerow() -> escreve uma linh

hearder_exist = os.path.isfile(filename)

with open(filename, 'a', encoding='utf-8', newline='') as csvfile:
    database_csv = writer(csvfile)

    if not hearder_exist:
        database_csv.writerow(['Título', 'Gênero', 'Duração'])

    filme = None
    while filme != 'sair':
        filme = input('Filme: ')
        if  filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração (min): ')
            database_csv.writerow([filme, genero, duracao])

with open(filename, 'a', encoding='utf-8') as csvfile:
    database_csv = writer(csvfile)
    filme = None
    # verifica se o arquivo está vazio
    if os.path.getsize(filename) == 0:
        # escreve o cabeçalho apenas se o arquivo estiver vazio
        database_csv.writerow(['Título', 'Gênero', 'Duração'])

    while filme != 'sair':
        filme = input('Filme: ')
        if  filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração (min): ')
            database_csv.writerow([filme, genero, duracao])



"""
from csv import DictWriter
import os

filename = 'filmes.csv'

with open(filename, 'w', encoding='utf-8') as csvfile:
    header = ['Título', 'Gênero', 'Duração']
    writer_csv = DictWriter(csvfile, fieldnames=header)
    writer_csv.writeheader()
    move = None
    while move != 'sair':
        move = input('Título: ')
        if move != 'sair':
            genre = input('Gênero: ')
            length = input('Duração: ')
            writer_csv.writerow({"Título": move, "Gênero": genre, "Duração": length})
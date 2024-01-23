"""
Lendo arquivo CSV

CSV - Comma Separeted Values Separados por Vírgula

# Separador por vírgula:
1, 2, 3, 4, 5
"str", "str"

# Separador por ponto e vírgula:
1; 2; 3; 4; 5
"str"; "str"


Link: http://dados.gov.br/dataset

A linguagem Python possui daus formas diferente de ler dados CSV:
    - reader -> Permite que iteremos sobre as linhas do arquiv CSV como lista;
    - DicReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts.



with open('lutadores.csv', encoding='utf-8') as csvfile1:
    data = csv.reader(csvfile1)
    data1 = []
    for row in data:
        for i in row:
            data1.append(i)
    print(data1)



"""
import csv

# # READER
# with open('lutadores.csv', encoding='utf-8') as csvfile:
#     database = csv.reader(csvfile)
#     next(database) # Pular cabeçalho
#     for row in database:
#         print(', '.join(row))

print('')

# DicReader
dictdata = []
with open('lutadores.csv', encoding='utf-8') as csvfile:
    database1 = csv.DictReader(csvfile)
    for row in database1:
        dictdata.append(row)

for _ in dictdata:
    print(_['Nome'])
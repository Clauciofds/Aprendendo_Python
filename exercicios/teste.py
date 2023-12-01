data = """name                                     year
Vicente Rodrigues dos Santos             1949
Nicolas Santos                           2010
Suzana Rodrigues                         1952
Heloisa Toledo                           2009
Herbet Toledo                            1995
Nicole Toledo                            2015
Willian Rodrigues                        1982
Fabiana Santos                           2016
Maria Bombi                              1951
Marcelo Roncolato                        1979
"""

# Dividir o texto em linhas e remover linhas em branco
lines = [line for line in data.split('\n') if line.strip()]

# Obter os títulos das colunas
columns = lines[0].split()

# Inicializar o dicionário
result_dict = {columns[0]: [], columns[1]: []}

# Preencher o dicionário com os dados
for line in lines[1:]:
    values = line.split()
    result_dict[columns[0]].append(" ".join(values[:-1]))
    result_dict[columns[1]].append(int(values[-1]))

# Exibir o dicionário resultante
print(result_dict)

print(result_dict["name"][0])

print("Vicente Rodrigues dos Santos" in result_dict["name"])

print(result_dict['year'])

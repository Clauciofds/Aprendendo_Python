"""
Faça um programa que receba como entrada o ano corrente e o nome de dois arquivo: um de entrada e outro
de saída. Cada linha do arquivo de entrada contém o nome de uma pessoa (ocupando 40 caracteres) e o seu
ano de nascimento. O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da pessoa seguida por um stringque representa a sua idade.

> Se a idade for menor do que 18 anos, escreva "menor de idade".
> Se a idade for maior que 18 anos, escreva "maior de idade"
> Se a idade for igual a 18 anos, escreva "entrando na maior idade"

"""

import datetime, os, re

# Define a month and year current
current_year = datetime.date.today().year


# Defeni Database empty
database = []
db_size = None

while db_size is None:
    try:
        db_size = int(input("Number of individuals interviewed: "))
    except ValueError as err:
        print(f"{err} - Digite um número inteiro")

def input_db():
    # Define database size
    for i in range(db_size):
        # Entering the user's name and year of birth
        key_name = input("Input name: ")
        key_year_birth = int(input("Year birth (YYYY): "))

        # Build dictionary
        database_inf = dict(name=key_name, year_birth=key_year_birth)
        database.append(database_inf)

    # Create file .txt
    file_exists = os.path.isfile("archives/database_years_old.txt")
    with open("archives/database_years_old.txt", "a") as file:
        if not file_exists:
            hearder = f"{'name':<40} {'year':>10}\n"
            file.write(hearder)
        for samplig in database:
            database_year_old = (f'{samplig["name"]:<40} {samplig["year_birth"]}\n')
            file.write(database_year_old)

    # print(type(database["year_bith"]))
    majority_define(database)
    main()

def majority_define(database):

    # Filter individuals who are 18 years older
    adults = list(filter(lambda data: (current_year - data["year_birth"]) > 18, database))

    # Print the result:
    for adult in adults:
        print(f"He or she is of legal age and has {adult['name']} is {adult['year_birth']} yeasr old")

    # Create text file .txt in specific directory
    file_exist = os.path.isfile("archives/adults_list.txt")
    with open("archives/adults_list.txt", "a") as file:
        if not file_exist:
            header = f"{'Nome':<40} {'Ano Nascimento':<15} {'Idade'}\n"
            file.write(header)
        for adult in adults:
            adults_list = (f'{adult["name"]:<40} {adult["year_birth"]:<15} {(current_year - adult["year_birth"]):^2}\n')
            file.write(adults_list)

def old_define(year_old, current_year):
    older = current_year - year_old
    if older < 18:
        return f'menor de idade - {older}'
    elif older > 18:
        return f'maior de idade - {older}'
    else:
        return f'entrando na maior idade - {older}'

def main():
    with open('archives/database_years_old.txt', 'r') as file:
        columns1, columns2 = file.readline().split()
        file = file.read().splitlines()
        file = tuple(file)
        database = []
        database1 = []
        for line in file:
            lines = re.sub(r'\s+', ' ', line)
            database.append(lines)

        for i in database:
            parts = i.rsplit(' ', 1)
            database1.append(parts)

        for user in database1:
            name, year_old_str = user
            year_old = int(year_old_str)
            majority = old_define(year_old, current_year)
            print(f'{name:<30}: {year_old:>4} - {majority:>3} anos')

input_db()

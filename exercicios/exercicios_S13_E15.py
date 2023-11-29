"""


"""

import datetime, os, csv

# Define a month and year current
month_year_current = datetime.date.today().strftime("%Y")
int_year = int(month_year_current)

# Defeni Database empty
database = []
db_size = None

while db_size is None:
    try:
        db_size = int(input("Number of individuals interviewed: "))
    except ValueError as err:
        print(f"{err} - Digite um número inteiro")

def input_db(name, year_birth):
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
    majority_define_read(database)



def majority_define(database):

    # Filter individuals who are 18 years older
    adults = list(filter(lambda data: (int_year - data["year_birth"]) > 18, database))

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
            adults_list = (f'{adult["name"]:<40} {adult["year_birth"]:<15} {(int_year - adult["year_birth"]):^2}\n')
            file.write(adults_list)

def majority_define_read(database):
    with open("archives/database_years_old.txt", "r") as file:
        dict_keys = file.readline().split()
        print(dict_keys)
        contents = file.readlines()
        contents.pop()
        print(contents)
        database = []
        for line in contents:
            values = line.split()
            database_inf = dict(dict_keys, values)
            database.append(database_inf)

    # Convert the year of birth to integers for comparison if necessary
    # database_int = [{"name": data["name"], "year": int(data["year"])} for data in database]

    print(database)




input_db(name="", year_birth="")



def majority_define_read(database):
    with open("archives/database_years_old.txt", "r") as file:
        dict_keys = file.readline().split()
        contents = file.read().split("\n")
        contents.pop()  # Remove last empty line
        database = []
        for line in contents:
            values = line.split()
            database_inf = dict(zip(dict_keys, values))
            database.append(database_inf)
    return database

import datetime
import re

current_year = datetime.date.today().year
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
main()



"""
Crie um programa em python que receba como entrada o número de alunos de um disciplina. Aloque dinamicamente em um
estrutura para armazenar as informações a respeito desses alunos: nome do aluno e sua nota final. Use nome com no
máximo 40 caracteres. Em seguida, salve os dados dos alunos em um arquivo binário. Por fim, leia o arquivo
e mostre o nome do aluno com maior nota.
"""

import os
import re

os.chdir(os.path.join('archives'))

def classroom_size():
    # Define database size
    while True:
        try:
            data_size = int(input('How many student will registered: '))
            break
        except ValueError as err:
            print(f"Valor incorreto! {err}")
    return data_size


def database(data_size, name_current):
    with open(name_current, "ab") as file:
        # Creata empty database
        data = []

        # Input names and studant's final notes
        for i in range(data_size):
            # Input studant's names
            while True:
                studants_name = input("Name: ")
                if len(studants_name) <= 40:
                    break
                else:
                    print("O nome dever ter menos de 40 carecteres")

            # Input studant's final notes
            while True:
                try:
                    final_notes = float(input("Final notes: "))
                    break
                except ValueError as err:
                    print(f"Valor incorreto! {err}")

            # Info database created
            datas_inf = dict(name=studants_name, note=final_notes)
            data.append(datas_inf)

        for inf in data:
           file.write(f"{inf['name']:<40}{inf['note']}\n".encode("utf-8"))


def file_name():
    # Define the file name
    name_current = input("Enter file name: ")
    name_current = re.sub(r"\s", "_", name_current.lower() + '.bin')

    # Check path
    file_exist = os.path.isfile(name_current)

    if not file_exist:
        # Input header
        with open(name_current, "wb") as file:
            hearder = f'{"Nome":<40}Nota final\n'.encode("utf-8")
            file.write(hearder)
    else:
        print("Classroom exist!")

    return name_current


def read_file(name):
    # Read current file and delete the first one
    studants = []
    with open(name, "rb") as file:
        contents = file.readlines()
        contents = contents[1:]

    for line in contents:
        contents = line.split()
        line_name = b' '.join(contents[:-1]).decode("utf-8") # Combine all parts except the last one
        line_note = float(contents[-1].replace(b",", b".")) # Converte brasilian decimal number
        studants.append((line_name, line_note))

    return studants

def max_final_note(studants):
    if not studants:
        return None
    max_note = max(studants, key=lambda x: x[1])
    return max_note[0:]



def main():
    name = file_name()
    size = classroom_size()

    database(size, name)

    current_studants = read_file(name)

    studants_with_max_note = max_final_note(current_studants)

    print(f"O aluno(a): {studants_with_max_note[0]} com maior nota {studants_with_max_note[1]}")



if __name__ == "__main__":
    main()
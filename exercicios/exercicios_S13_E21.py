"""
Crie um programa em pythonque receba como entrada o número de alunos de um disciplina. Aloque dinamicamente em um
estrutura para armazenar as informações a respeito desses alunos: nome do aluno e sua nota final. Use nome com no
máximo 40 caracteres. Em seguida, salve os dados dos alunos em um arquivo binário. Por fim, leia o arquivo
e mostre o nome do aluno com maior nota.
"""

import os
import re

os.chdir(os.path.join('archives'))


def name_file():

    # Define and create a new file for database
    name_of_archive = input('Enter with file name: ')
    file_exist = os.path.isfile(name_of_archive)
    if not file_exist:
        # Changing the name of the system's default compatible file
        name_of_archive = re.sub(r'\s', '_', name_of_archive.lower()) + '.' + 'bin'
        with open(name_of_archive, "wb") as file:
            header = f'{"Nome":<40}Nota Final\n'.encode('utf-8')
            file.write(header)
    else:
        print('Already registered class')

    return name_of_archive


def database(classroom_size):
    data = []
    for i in range(classroom_size):
        while True:
            studant_name = input('Name: ')
            if len(studant_name) <= 40:
                break
            else:
                print('The name must be less than 40 characters')
        try:
            final_note = float(input('Final note: '))
        except ValueError as err:
            print(f'Tupe final Note - {err}')

        # Dictionary create for contents file
        inputs = dict(name=studant_name, note=final_note)
        data.append(inputs)

    with open(name_file(), 'ab') as file:
        for inf in data:
            file.write(f'{inf["name"]:<40}{inf["note"]}\n'.encode('utf-8'))

    return data


def max_note(name_of_archive):
    # Read binary file
    current_file = name_of_archive
    with open(current_file, 'rb') as file:
        lines = file.readlines()
        lines = lines[1:]

        # Initialize the variables before the loop
        name = ''
        final_note = 0

        for line in lines:
            # Define the studant with max final note
            contents = line.split()
            current_name = b' '.join(contents[:-1]).decode('utf-8')  # Combines all parts except the last one
            current_final_note = float(contents[-1].replace(b',', b'.'))  # Convert the note to a decimal number

            if current_final_note > final_note:
                name = current_name
                final_note = current_final_note

    return name, final_note


def main():
    file_name = name_file()

    # Define how many stunds will be resgistered for loop
    while True:
        try:
            classroom_size = int(input('How many studant will be registered: '))
            break
        except ValueError as err:
            print(f'Valor incorreto! {err}')

    database(classroom_size)

    max_final_note = max_note(file_name)
    print(f'Name: {max_final_note[0]} - Max Final Nota {max_final_note[1]}')

    with open(file_name, 'rb') as file:
        print(file.read().decode('utf-8'))


if __name__ == '__main__':
    main()


"""
Faça um programa que receba como entrada o nome de um arquivo de entrada e o nome de um arquivo de saída. O arquivo de
entrada contém o nome de aluno ocupando 40 caracteres e três inteiros que indicam suas notas. O programa deverá
ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome do aluno e as suas notas em ordem crescente.
"""

import os
import re

os.chdir(os.path.join("archives"))

def input_file_name():
    # Create an input file name
    while True:
        input_file = input("Input file: ")
        if input_file != "":
            input_file = re.sub(r"\s", "_", input_file.lower() + ".txt")
            break
        else:
            print("Empty name!")

    return input_file


def output_file_name():
    # Create an output file name

    while True:
        output_file =  input("Output file: ")
        if output_file != "":
            output_file = re.sub(r"\s", "_", output_file.lower() + ".txt")
            break
        else:
            print("Empty name!")

    return output_file


def studants_database(input_file, data_size):
    # Create an empty library
    data = []

    # Check file existed
    file_exist = os.path.exists(input_file)

    with open(input_file, "a") as file:
        # Print header in new files
        if not file_exist:
            header = f"{'Name':<40}Note\n"
            file.write(header)

        for i in range(data_size):
            # Input stunts names
            while True:
                studants_name = input("Name: ")
                if len(studants_name) <= 40:
                    break
                else:
                    print("The name must be less than 40 characters!")

            # Enter three integers that indicate your grades
            while True:
                try:
                    final_note = int(input("Note: "))
                    break
                except ValueError as err:
                    print(f"Incorret value: {err}")

            data.append((studants_name, final_note))

        # Save registered information to the file
        for i in range(data_size):
            contents = f"{data[i][0]:<40}> {data[i][1]}\n"
            file.write(contents)

def read_file(input_fie):
    # Create an empty library's
    file_contents = []
    with open(input_fie, "r") as file:
        # Read the file and skip the header
        lines = file.readlines()
        lines = lines[1:]

    for line in lines:
        line = re.sub(r"\s+", " ", line)
        contents = line.split(">")
        line_name = contents[0]
        line_note = int(contents[1])
        file_contents.append((line_name, line_note))

    return file_contents

def sort_ascending(out_file, file_contents):
    # Always write a new file with new information
    with open(out_file, "w") as file:
        # Creata header
        hearder = f"{'Name':<40}Note\n"
        # Ascending ordering of test scores to save
        sorted_contents = "".join([f"{name:<40}{note}\n" for name, note in sorted(file_contents, key=lambda x: x[1])])
        file.write(
            f"{hearder}"
            f"{sorted_contents}"
        )

def main():
    name_current = input_file_name()
    data_size = int(input("How many studants: "))

    studants_database(name_current, data_size)

    output_name = output_file_name()
    contents = read_file(name_current)

    sort_ascending(output_name, contents)

if __name__ == "__main__":
    main()

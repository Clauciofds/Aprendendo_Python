"""
Crie um program que receba como entrada o número de alunos de uma disciplinha. Aloque dinamicamente dois vetores
para armazenar as informações a respeito desses alunos. O primeiro vetor contém o nome dos alunos e o segundo contém
suas notas finais. Crie um arquivo que armazene, a cada linha, o nome do aluno e sua nota final. Use nomes com no
máximo 40 caracteres. Se o nome não contém 40 caracters, complete com espaços em branco.
"""
import os

os.chdir(os.path.join('archives'))

# size of the database that will be registered this moment
class_studant = int(input('How many students will be registered: '))

for i in range(class_studant):
    file_exist = os.path.isfile('database_classroom.txt')
    with open('database_classroom.txt', 'a') as file:
        if not file_exist:
            file.write(f'{"Nome":<40}Nota\n')
        name = input('Studant name: ')
        try:
            final_note = float(input('Final note: '))
        except ValueError as err:
            print(f'Digite a nota do aluno: {err}')
        file.write(f'{name:<40}> {final_note:>.2f}\n')
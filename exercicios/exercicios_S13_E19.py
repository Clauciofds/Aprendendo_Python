"""
Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de diversos
alunos (da seguinte forma: NOME: João NOTA: 8), um aluno por linha.
Mostre na tela o nome e a nota do aluno que possui a maior nota.
"""
# -*- coding: utf-8 -*-
import os

os.chdir(os.path.join('archives'))

def note_extract(line):
    # Function to extract the note from a line
    nome, note_str = line.split('NOTA:')
    return float(note_str)

with open('boletim_stunds.txt', 'r') as file:
    # Read all lines of the file
    lines = file.readlines()

    # Find the line with the highest score using the note_extract() function as the key
    max_note_line = max(lines, key=note_extract)

    # Extract name and grade from the line with the highest grade
    name, note = max_note_line.split('NOTA:')
    name = name.strip()
    note = float(note)

    # Display the name and grade of the student with the highest grade on the screen
    print(f'O aluno com a maior note é: \n'
          f'"{name} - NOTA: {note}".')
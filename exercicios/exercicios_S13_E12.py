"""
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras
neste arquivo. Escreva também quantos vezes cada letra ocorre no arquivo (ignorando as letras com acento).
Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.
"""
import os

# Open and read text file.
with open("archives/densidade_demografica.txt", "r") as file:
    # Save de text content in variable
    content = list(file.read())
    # Count the letters of the text
    file_size = len(content)
    file.seek(0)
    # Count the lines of the text
    numbers_lines = len(file.readlines())
    file.seek(0)
    # Counts the words of the text
    numbers_words = len(file.read().split())

    # Save alphabet in variable
    alphabet = "abcdefghijlkmnopqrstuvwyzABCDEFGHILJKMNOPQRSTUVWXYZ"
    # Create a empty dictionary
    freq = {}

    # Interacts with the contents of the text file to count the letters
    for char in content:
       if char in freq:
           freq[char] += 1
       else:
           freq[char] = 1

    # Interacts with the dictionary and order for print
    for i in sorted(freq):
        if i in alphabet:
            print(f"Letter: {i} - Frequency: {freq[i]}")

    print(f"Total character of text file: {file_size:,.0f}")
    print(f"Sum of lines: {numbers_lines}")
    print(f"Total sum words: {numbers_words}")

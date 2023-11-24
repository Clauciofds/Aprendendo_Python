"""
Faça um programa no qual o usuário informa o nome de arquivo e uma palavra, e retorne o número
de vezes que aquale palavra aparece no arquivo.

"""
import os

# Entry for search file name and word
file_name = input("Search: ")
file_name += ".txt"
word_search = input("Word to search: ")

# Changing directory of work
os.chdir(os.path.join("archives"))

try:
    # If the search file exists, it will be opened
    with open(file_name, "r") as archive:
        # Reads and saves the file in the
        content = archive.read()
    # Create the empty variable
    total_word = 0

    # Interact with the string
    if word_search in content:
        # Look for and count the search word
        count = content.count(word_search)
        total_word += count

    # Result search
    print(total_word)

except FileNotFoundError as err:
    print(err)
except:
    print("erro")

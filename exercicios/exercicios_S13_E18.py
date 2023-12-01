"""
Faça um programa que leia um arquivo de texto contendo o nome e o preço de diversos produtos
(separados por linhas), e calcule o total da compra
"""

import os, locale

# Checking directory
os.chdir(os.path.join("archives"))
file_exist = os.path.isfile("shopping_list.txt")

# Createde .txt file with shopping list
with open("shopping_list.txt", "a") as file:
    # Print if text file not exist
    if not file_exist:
        file.write("Produt-Price\n")

    # Input data
    while True:
        try:
            produt_name = input("Produt: ")
            price = float(input("Price: "))
            break_list = input("Read (Y/N): ")
        except ValueError as err:
            print("Valor incorreto", err)

        if break_list != "y" and break_list != "Y":
            file.write(f"{produt_name}-{price}\n")
        else:
            # If list complety than save the last item before break
            file.write(f"{produt_name}-{price}\n")
            break

# Configuring printing for local currency
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Read shopping list
with open("shopping_list.txt", "r") as file:
    column_1, column_2 = file.readline().split("-")
    lines = file.readlines()
    total = 0
    for line in lines:
        produt, price = line.split("-")
        price = float(price)
        total += price
    print(f'{column_1:<25} {column_2:>2}')
    for line in lines:
        produt, price = line.split('-')
        price = float(price)
        print(f'{produt:<15} {locale.format_string("R$ %.2f", price, grouping=True):>15}')
    print(f"Total: {locale.format_string('R$ %.2f', total, grouping=True):>24}")

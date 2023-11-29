"""
Faça um programa que recebe um vetor de 10 números, converta cada um desses números
para binário e grave a sequência de 1s e 0s em um arquivo texto. Cada número deve ser
gravado em uma linha.

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("archives/binary_numbers.txt", "w") as file:
    for number in numbers:
        binary = bin(number)[2:]
        file.write(binary + "\n")

with open("./archives/binary_numbers.txt", "r") as file:
    print(file.read())

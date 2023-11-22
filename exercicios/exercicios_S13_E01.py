import os

# print(os.getcwd())

with open("archives/exercice_S13_E1.txt", "a") as archive:
    while True:
        word = input("Chose your word or type O for exit.\n"
                     "Type were: ")
        if word != "o" and word != "O":
            archive.write(f"{word}\n")
        else:
            print("")
            break

with open("archives/exercice_S13_E1.txt") as archive:
    print(archive.read())

print(f"The archive is closed?\n"
      f"{archive.closed}")
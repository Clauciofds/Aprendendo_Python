with open("archives/densidade_demografica.txt", "r") as archive:
    body_list = archive.read()
    vowel = "?"
    modified_content = ""
    for char in body_list:
        if char in vowel:
            modified_content += "ã"
        else:
            modified_content += char
        with open("archives/densidade_demografica.txt", "w") as new_archive:
            new_archive.write(modified_content)

with open("archives/densidade_demografica.txt") as archive:
    print(archive.read())


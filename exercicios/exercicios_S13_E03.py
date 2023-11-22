with open("archives/exercice_S13_E1.txt", "r") as archive:
    consonant_vowel = archive.read()
    # vowel = vowel.split()
    # print(vowel)
    counter_consonant = 0
    counter_vowel = 0
    for i in consonant_vowel:
        if i in ["a", "e", "i", "o", "u"]:
            counter_vowel += 1
        else:
            counter_consonant += 1
    print(f"Word list has a total of {len(consonant_vowel)} words\n"
          f"and has {counter_consonant} consonant\n"
          f"and {counter_vowel} vowel")

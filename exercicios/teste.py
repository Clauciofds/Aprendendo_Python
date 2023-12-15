lista = [['Maria Silva', '(11) 98765-4321', '15 de março'], ['João Santos', '(21) 98765-1234', '22 de julho'],
 ['Ana Oliveira', '(31) 97654-3210', '10 de janeiro'], ['Lucas Pereira', '(41) 96543-2109', '5 de setembro'],
 ['Juliana Costa', '(51) 95432-1098', '18 de abril'], ['Rafael Lima', '(61) 94321-0987', '7 de junho'],
 ['Camila Souza', '(71) 93210-8765', '20 de outubro'], ['Thiago Oliveira', '(81) 92109-8765', '12 de fevereiro'],
 ['Larissa Santos', '(91) 91087-6543', '25 de agosto'], ['Felipe Rocha', '(01) 98765-4321', '30 de dezembro'],
 ['Bruna Costa', '(02) 98765-1234', '3 de julho'], ['André Pereira', '(03) 97654-3210', '14 de maio'],
 ['Letícia Lima', '(04) 96543-2109', '8 de novembro'], ['Gustavo Oliveira', '(05) 95432-1098', '11 de setembro'],
 ['Vanessa Santos', '(06) 94321-0987', '19 de janeiro'], ['Pedro Souza', '(07) 93210-8765', '23 de março'],
 ['Carolina Silva', '(08) 92109-8765', '9 de agosto'], ['Gabriel Rocha', '(09) 91087-6543', '2 de abril'],
 ['Amanda Costa', '(10) 98765-4321', '17 de junho'], ['Bruno Lima', '(11) 98765-1234', '1 de outubro']
 ]

info_to_search = input("Search: ").lower()

list_to_names = []
print(lista[0][0][0].lower())

for word in lista:
    if info_to_search == word[0][0][0].lower():
        print(word)
        print(lista[0])
        list_to_names.append(word)
        list_to_names = sorted(list_to_names)

if list_to_names:
    for contact in list_to_names:
        print(f'{contact[0]} - {contact[1]} - {contact[2]}')


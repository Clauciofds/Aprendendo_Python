def intercalar(string1, string2):
    string1 = input("Digite uma palavra: ")
    string2 = input("Digite outra palavra: ")
    resultado = []

    lista_string1 = list(string1)
    lista_string2 = list(string2)

    tamanho_menor = min(len(lista_string1), len(lista_string2))

    for i in range(tamanho_menor):
        resultado.append(lista_string1[i])
        resultado.append(lista_string2[i])

    resultado.extend(lista_string1[tamanho_menor:])
    resultado.extend(lista_string2[tamanho_menor:])

    resultado_string = ''.join(resultado)
    return print(resultado_string)

intercalar(string1='a', string2='b')
def soma_alfabetica(text):
    resultado = ''
    for letra in text:
        if letra.isalpha():
            if letra == 'z':
                resultado += 'a'
            elif letra == 'Z':
                resultado += 'A'
            else:
                resultado += chr(ord(letra) + 1)
        else:
            resultado += letra
    return resultado

texto_original = input("Digite o texto: ")
texto_soma_alfabetica = soma_alfabetica(texto_original)
print("Texto após a soma alfabética:", texto_soma_alfabetica)

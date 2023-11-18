def concatena_strings(str1, str2 , N):
    # Verifica se N é maior ou igual ao comprimento de str2
    if N >= len(str2):
        str1 += str2 # Concatena str2 inteira em str1
    else:
        str1 += str2[:N] # Concatena apenas os primeiros N caracteres de str2 em str1
    str1 += '\0'
    return str1

# Exemplo de uso funcao

str1 = 'Ola, '
str2 = 'Mundo!'
N = 3

resultado = concatena_strings(str1, str2, N)
print(resultado) # Saída: "Ola, Mun\0"
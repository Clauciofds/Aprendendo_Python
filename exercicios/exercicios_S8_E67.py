import msvcrt

def ler_string_do_teclado(vetor, tamanho_maximo):
    i = 0 # Inicializa o indice do vetor

    while i < tamanho_maximo:
        char = input() # Lê um caractere do teclado

        # Verifica se o caractere é Enter (tecla 'Enter' pressionado)
        if not char:
            break # Sai do loop se Enter for pressionado

        vetor[i] = char[0] # Armazena o caractere no vetor
        i += 1 # Incrementa o indice

    return vetor[:i]

tamanho_maximo = 50
vetor = [''] * tamanho_maximo

resultado = ler_string_do_teclado(vetor, tamanho_maximo)

print("String lida: ", ''.join(resultado))

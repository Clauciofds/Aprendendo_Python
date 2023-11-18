def ler_string_do_teclado(vetor, tamanho_maximo):
    i = 0  # Inicializa o índice do vetor

    while i < tamanho_maximo:
        char = input()  # Lê um caractere do teclado

        # Verifica se o caractere é Enter (tecla 'Enter' pressionada)
        if not char:
            break  # Sai do loop se Enter for pressionado

        vetor[i] = char[0]  # Armazena o caractere no vetor
        i += 1  # Incrementa o índice

        # Certifique-se de que o vetor termina com um caractere nulo
        if i < tamanho_maximo:
            vetor[i] = '\0'

    return vetor[:i]


# Função de exemplo para ler uma string de até 50 caracteres
tamanho_maximo = 50
vetor = [''] * tamanho_maximo  # Inicializa o vetor com caracteres nulos
ler_string_do_teclado(vetor, tamanho_maximo)

# Imprime a string lida do teclado
print("String lida:", ''.join(vetor))

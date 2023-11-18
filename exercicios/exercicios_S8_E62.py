def tamanho(frase, tamanho):
    tamanho[0] = len(frase)

# Exemplo de uso:
minha_string = "Hello, world!!!"
tamanho_da_string = [0]  # Uma lista para armazenar o tamanho da string

tamanho(minha_string, tamanho_da_string)

print("O tamanho da string é:", tamanho_da_string[0])

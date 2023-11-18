lista = [1, 2, 3, 4, 5]
num_variaveis = len(lista)

for i, elemento in enumerate(lista):
    nome_variavel = f'var{i + 1}'
    globals()[nome_variavel] = elemento

print(var1)  # Imprimirá 1
print(var2)  # Imprimirá 2
print(var3)  # Imprimirá 3
print(var4)  # Imprimirá 4
print(var5)  # Imprimirá 5

'''
Neste exemplo, usamos a função enumerate para obter tanto o índice quanto o 
elemento da lista. Criamos um nome de variável dinâmico nome_variavel usando 
o valor do índice mais 1 (pois os índices começam em 0, mas queremos variáveis 
numeradas a partir de 1). Então, usamos a função globals() para adicionar 
essa variável ao escopo global com o valor do elemento correspondente.

Lembre-se de que essa abordagem pode ser confusa e tornar o código mais difícil 
de entender e manter. Em vez disso, considere usar listas ou dicionários para 
armazenar os valores e acessá-los de forma mais organizada e eficiente.

'''

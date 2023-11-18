# def comparar(palavra1='a', palavra2='b'):
#
#     palavra1 = input('Digite alguma coisa: ')
#     palavra2 = input('Digite outra coisa: ')
#
#     if palavra2 == palavra1:
#         return print(f'> {palavra1} é igual a {palavra2}')
#     else:
#         return print(f'> {palavra1} é diferente de {palavra2}')

def comparar(*args):
    palavras = []
    palavra = 1
    for palavra in range(2):
        palavra = input(f'{palavra + 1} > Digite algo: ')
        palavras.append(palavra)

    if palavras[0] == palavras[1]:
        print(f'> {palavras[0]} é igual a {palavras[1]}')
    else:
        return print(f'> {palavras[0]} é diferente de {palavras[1]}')

comparar()
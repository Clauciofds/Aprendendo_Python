"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas por todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde fora declarada.

Para declarar variáveis em Python fazemos:
- nome_da_variável = valor_da_variável


"""

numero = 42
print(numero)
print(type(numero))

numero = 'Claucio'
print(f'\n{numero}')
print(type(numero))

nao_exito = '\nOi'
print(nao_exito)

numero = 42

if numero > 10:
    novo = numero + 10
    print(f'\n{novo}')

print(type(novo))

no_num = input('\nDigite um número: ')
print(no_num, type(no_num))
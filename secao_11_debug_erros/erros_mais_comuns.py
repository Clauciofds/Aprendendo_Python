"""
Erros mais comuns em Python

Atenção! É importante prestar a atenção e aprender a ler as saídas de erros geradas pela execução
do noss código.

Exemplo de SYntaxError

def funcao:
    print('Geek University')

def = 1

NameError - Ocorre quando uma variável ou função não foi definida.

print(geek)

a = 18

if a < 10:
    msg = 'E maior que 10'

print(msg)

Exemplo TypeError - Ocorre quando um função/operação é aplicada a um tipo errado.

print('Geek' + [])

Exmplo IndexError - Ocorre quando tentando acessar um elemento em um lista ou outro tipo de indexado utilizando

um indice invalido.

lista = ['Geek']
print(lista[1])

# Exemplo ValueError
print(int('Geek'))

# Exemplo KeyError - Ocorre quando tentamos acessar alguma tipo de chave que não exite.
dic = {}
print(dic['Geek'])

# Exemplo - AttributeError - Ocorre quando um variável não tem um função não é apropriada para a variável
tupla = (1, 2, 3, 4)
print(tupla.sort())


"""
# Exemplo - IndentationError -  Ocorre quando não respeitamos a indentação do Python (4 espaços)
def nova():
    print('Geek')
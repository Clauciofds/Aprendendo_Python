"""
**kwargs

Exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.
"""

# EXEMPLO 01

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marco='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# EXEMPLO 02
print("")
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return print('\nVocê recebeu um cumprimento Pythônico Geek!')
    return print(f'\nNão tenho certeza...')

cumprimento_especial()
cumprimento_especial(geek='Python')
cumprimento_especial(geek='Oi')
cumprimento_especial(geek='especial')

"""
Nas nossas funções, podemos ter um ordem obrigatória de syntax

- Parâmetros obrigatórios;
- *args;
- Parâmetro default (não obrigatórios);
- **kwargs

"""
# EXEMPLO 03
print("")

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'\n{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solterio')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 2, 4, 5, 6)
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 3, 4, 5, java=False, python=True)


# Ordem correta de parametros:
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    print("")
    return [a, b, args, instrutor, kwargs]

# Ordem incorreta:
def mostr_infoe(a, b, instrutor='Geek', *args, **kwargs):
    print("")
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {sobrenome: 'University', cargo:'Instrutor'}

"""

print(mostra_info(1, 2, 3, sobrenome='Univesity', cargo='Instrutor'))
print(mostr_infoe(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return print(f"\n{kwargs['nome']} {kwargs['sobrenome']}")

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

mostra_nomes(**nomes)


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(f'\n{a + b + c}')

lista = [1, 2, 3]
tupla = 1, 2, 3
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3, nome='Claucio')

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)
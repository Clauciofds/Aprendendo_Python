print('V1')
def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Claucio'))
print(cumprimenta_v1(nome='Cleiton'))


print(F'\nV2')
# Parametros posicionais
def cumprimenta_v2(nome, /):
    return f'Olá {nome}'

print(cumprimenta_v2('Claucio'))
# print(cumprimenta_v2(nome='Cleiton'))

print('\nV3')


def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('Universaty', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))


print('\nV4')
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Geek'))
print(cumprimenta_v4('Felicity', 'Bem vinda'))
# print(cumprimenta_v4('University', mensagem='Hello'))


print('\nV5')
# Parâmetro obrigatórios
def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


print(cumprimenta_v5(nome='Claucio'))
print(cumprimenta_v2('Cleiton'))


print('\nV6')
def cumprimenta_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimenta_v6('Claucio', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimenta_v6('Cleiton', mensagem2='tenha um bom dia'))
print(cumprimenta_v6('Geek', 'Oi', mensagem2='tenha um bom dia'))

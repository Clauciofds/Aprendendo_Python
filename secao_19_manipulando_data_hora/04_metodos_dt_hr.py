"""
Métodos data hora:

# Marcando o tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphensio
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)



"""

import datetime
import timeit

agora = datetime.datetime.now()  # Neste caso pode-se especificar um time zone ou fuso horário.
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

print('')

# Especifica uma data especificada a exatos 00 horas
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

print('')

# Encontrar o dia da semana, weekday()
# Dias da semana na função weekday começam em 0 = segunda-feira
dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

print(f'Manuntenção será na: {dias_semana[manutencao.weekday()]}')

print('')

# aniversario = input('Data (dd/mm/aaaa): ')
#
# aniversario = aniversario.split('/')
#
# aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
#
# dias_aniver = aniversario - datetime.datetime.today()
#
# print(f"Faltam {dias_aniver.days}, que será no dia da semana {dias_semana[aniversario.weekday()]}")

# data_nasc = input('Dia nascimento (dd/mm/aaaa): ')
#
# data_nasc = data_nasc.split('/')
#
# data_nasc = datetime.datetime(year=int(data_nasc[2]), month=int(data_nasc[1]), day=int(data_nasc[0]))
#
# # Calcula a idade em anos
# idade = datetime.datetime.now().year - data_nasc.year
#
# # Calcula a idade em meses
# idade_meses = datetime.datetime.today().month - data_nasc.month
# idade_meses += 12
#
# # Calcula a idade em dias
# idade_dias = datetime.datetime.today().day - data_nasc.day
# idade_dias += datetime.datetime.today().day
#
# # Se o mês atua form menor que o mês de nascimento ou se o mês for igual e o dia atual for menor que o dia
# # de nascimento usa-se os parametros ajustado a idade e os meses atuais (idade_meses, idade_dias)
# if datetime.datetime.today().month < data_nasc.month or (
#         datetime.datetime.today().month == data_nasc.month and data_nasc.day < data_nasc.day
# ):
#     print(
#         f'Nasceu em um(a) '
#         f'{dias_semana[data_nasc.weekday()]} '
#         f'à {idade - 1} anos e {idade_meses} meses e {idade_dias} dias.'
#     )
# else:
#     print(f'Nasceu em um(a) {dias_semana[data_nasc.weekday()]} à {idade} anos.')

print("")
# Formatação de data
hoje = datetime.datetime.now().strftime('%d de %B de %Y')  # O B maiúsculo imprimo o nome do mês em ingles por extenso.

print(hoje)

dia_do_mes = datetime.datetime.today().strftime("%B")

dias_semana_ingles = {
    "January": "Janeiro",
    "February": "Fevereiro",
    "March": "Março",
    "April": "Abril",
    "May": "Maio",
    "June": "Junho",
    "July": "Julho",
    "August": "Agosto",
    "October": "Outubro",
    "November": "Novembro",
    "December": "Dezembro"
}

print(f'Dia {datetime.datetime.now().day} de {dias_semana_ingles[dia_do_mes]} de {datetime.datetime.today().year}')

print("")
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(from_lang='english', to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))

# Usando a função strptime para receber uma str e transformar em data

print(datetime.datetime.strptime('17/08/1973', '%d/%m/%Y').strftime('%d/%m/%Y'))

import os, time

# current_time = datetime.datetime.now().strftime('%H:%M:%S')
#
# print(current_time)
# while True:
#     for _ in current_time:
#         print(
#             datetime.datetime.now().strftime('%H:%M:%S')
#         )
#         time.sleep(1)
#         os.system('cls')

# Trabalhando com horas time()
almoco = datetime.time(12, 0, 0)
print(f'\n{almoco}')

import functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))

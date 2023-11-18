from datetime import datetime

data_atual = datetime.now()
dia = data_atual.day
mes = data_atual.month
ano = data_atual.year
def data_para_texto(dia, mes=data_atual.month, ano=data_atual.year):

    mes_tem_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]

    if dia > 30 or (mes == 2 and dia > 29) or (mes != 2 and mes in mes_tem_31_dias):
        print(f'Este mês não tem 31 dias. Digite outro!')
    else:
        data_formatada = f'{dia} de {meses[mes - 1]} de {ano}'
        print(f'Data: {data_formatada}')


data_para_texto(3, 2)

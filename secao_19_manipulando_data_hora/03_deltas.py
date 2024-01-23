"""
Operação com datetime


"""

import datetime

data_atual = datetime.datetime.now()

aniversario = datetime.datetime(2024, 8, 17)

tempo_ate_aniver = aniversario - data_atual

print(type(tempo_ate_aniver))
print(repr(tempo_ate_aniver))
print(tempo_ate_aniver)
print(tempo_ate_aniver.days, tempo_ate_aniver.seconds // (60 ** 2))

# Determinando uma data de vencimento de boleto.

data_compra = data_atual

print(f'Comprado: {data_compra.strftime("%d/%m/%y")}')

regra_boleto = datetime.timedelta(days=3)

print(f'Vencimento em {regra_boleto.days} dias')

vencimento = data_compra + regra_boleto

print(f'Vencimento: {vencimento.strftime("%d/%m/%Y")}')

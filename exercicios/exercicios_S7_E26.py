from statistics import stdev as sd

amostra = []
indice = 1

tamanho_da_amostra = int(input('Qual tamanho da amostragem: '))
resultado_esperado = float(input('Resultado esperado: '))

existe_tolerancio = input('Medição possui uma tolerância aceitavel (S/N): ')
existe_tolerancio = existe_tolerancio.upper()

if existe_tolerancio == 'S':
    tol_maior = float(input('Tolerância maior: '))
    tol_menor = float(input('Tolerância menor: '))

for valor in range(tamanho_da_amostra):
    valor = float(input('Desvio da amostra: '))
    desvio_encontrado = resultado_esperado + valor
    amostra.append(desvio_encontrado)


print(f'\nTamanho da amostra: {tamanho_da_amostra}')

if existe_tolerancio == 'S':
    print(f'Dimensão:  {resultado_esperado}')
    print(f'Tolerância +/-:   {tol_maior:.2f}/{tol_menor:.2f}')
    print(f'\n| Amostra | Tol < | Resulta | Tol > |')
    for val in amostra:
        print(f'|{indice:^9}|{resultado_esperado + tol_menor:^7.2f}|{val:>7.2f}  |{resultado_esperado+tol_maior:^7.2f}|')
        indice += 1
else:
    print(f'\n| Amostra | Resulta |')
    for val in amostra:
        print(f'|{indice:^9}|{val:>6.2f}  |')
        indice += 1

print('| Desvio Padrão: ', round(sd(amostra), 2),' |')


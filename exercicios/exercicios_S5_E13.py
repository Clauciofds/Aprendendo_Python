import numpy as np

# ENTRADAS
while True:
    cadastros = int(input('Digite as avaliações que serão processadas entre 2 e 6: '))
    if cadastros >= 2 and cadastros <= 6:
        break

pesos = []
media_ponderada = []

for i in range(cadastros):
    while True:
        nota = float(input('\nNota da prova entre 0 e 100: '))
        if nota >= 0 and nota <= 100:
            media_ponderada.append(nota)
            break
        else:
            print('Errouuuu!!!!')
    while True:
        peso = float(input('Digite o peso da nota entre 1 e 2: '))
        if peso >= 1 and peso <= 2:
            pesos.append(peso)
            break
        else:
            print('Errouuu!!')

# print(media_ponderada, pesos)

# CALCULOS
media_ponderada = np.average(media_ponderada, weights=pesos)
# print(media_ponderada, type(media_ponderada))

# SAÍDAS
if media_ponderada >= 60.0:
    print(f'\nA média ponderada é: {media_ponderada:.2f} \U0001F44D\nO aluno(a) está aprovado')
else:
    print(f'\nA média do aluno é: {media_ponderada:.2f} \U0001F44E\nO aluno(a) está reprovada')
    
import numpy as np

notas = []
pesos = []

while True:
    cadastros = int(input('Quantas avaliações serão processadas (2 ou 3): '))
    if cadastros >= 2 and cadastros <=3:
        break
    else:
        print('Errooouuu!!!')

for i in range(cadastros):
    while True:
        nota = float(input('\nDigite a nota (0-10): '))
        if nota >=0 and nota<=10:
            notas.append(nota)
            break
        else:
            print('Errooouuu!!!')

    while True:
        peso = int(input('\nQual avaliação está sendo processada? \
                          \n1 - Trabalho Laborátorial \
                          \n2 - Avaliação Semestral \
                          \n3 - Avaliação Final \
                          \n\nDigite a opção aqui: '))
        if peso >= 1 and peso <= 3:
            pesos.append(peso)
            break
        else:
            print('Errroouuuu!!!')

notas = np.average(notas, weights=pesos)

print('')
if notas < 3:
    print(f'Aluno REPROVADO: {notas:.2f}')
elif notas >=3 and notas < 5:
    print(f'Aluno EM RECUPERAÇÃO: {notas:.2f}')
else:
    print(f'Aluno APROVADO: {notas:.2f}')
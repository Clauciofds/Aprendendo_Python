import math, statistics

#math.prod - retorna o produto de um container numério

nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

print('')

# math.isqrt - retorna a parte inteira da raiz quadrada de um número
print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))

print('')

#math.dist - retorna a distância euclidiana entr dois pontos, 3D ou 2D

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

print('')

# math.hipot - retorna a hipotenusa, ou norma Euclidiana
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))

print('')

# statistics.fmean - calcula a média de números reais
valores_reais = [1.45, 6.767, 3.45]
valores_inteiros = [1, 6, 3, 89]
valores_fracionados = [1/2, 4/8, 8/16]

print(statistics.mean(valores_reais))
print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))
print(statistics.mean(valores_inteiros))
print(statistics.fmean(valores_fracionados))
print(f'{statistics.mean(valores_fracionados):05.2f}')

print('')

seq1 = 'Claucio Fernando Donizete dos Santos'
seq2 = 'As funções fmean() e mean() são usadas para calcular a média aritmética de um conjunto de dados numéricos. A média aritmética é a soma dos dados dividida pelo número de pontos de dados. É uma medida da localização central dos dados em um conjunto de valores que variam em alcance.'
seq2 = seq2.split()
print(seq2)
print(statistics.multimode(seq1))
print(statistics.multimode(seq2))

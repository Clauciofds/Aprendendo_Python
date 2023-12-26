"""
Introduzindo condicionais lógica para as list

"""

numeros = [1, 2, 3, 4, 5, 6]

# 1
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Qualquer número par móduloa de 2 é 0 e o 0 em python o resultado 0 e False. not False == True para números pares.
pares = [numero for numero in numeros if not numero % 2]

impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero / 2 if numero % 2 == 0 else numero * 2 for numero in numeros]
res_int = [round(x) for x in res]
res_int_join = ' '.join(str(int(numero)) for numero in res)
teste = [numero * 2 for numero in res_int_join if numero != ' ']
teste1 = list(teste)
teste2 = [int(x) for x in teste1]


print(res)
print(res_int, type(res_int))
print(res_int_join, type(res_int_join))
print(teste)
print(teste1)
print(teste2, type(teste2))

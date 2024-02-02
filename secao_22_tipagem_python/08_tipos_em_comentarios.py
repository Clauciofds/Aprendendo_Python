import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8.5))

# print(circunferencia('dureza'))

def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho('texto=45', alinhamento=True)
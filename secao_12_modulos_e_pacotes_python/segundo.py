import primeiro

def funcao2():
    primeiro.funcao1()

if __name__ == '__main__':
    funcao2()
    print(f'\nsegundo.py está sendo executado diretemente. {__name__}')
else:
    print(f'\nsegundo.py foi importado: {__name__}')

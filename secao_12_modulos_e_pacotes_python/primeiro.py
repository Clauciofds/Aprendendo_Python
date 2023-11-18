def funcao1():
    print("Geek Univeserstiy - primeiro.py")

if __name__ == '__main__':
    funcao1()
    print(f'\nprimeiro.py está sendo executado diretamente: {__name__}')
else:
    print(f'\nprimeiro.py foi importado: {__name__}')

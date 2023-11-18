chaves = ['sexo', 'cor_dos_olhos', 'idade']
valores = [['f', 'a', 33], ['m', 'v', 21], ['f', 'c', 19]]


resultado = [{chaves[i]: valor[i] for i in range(len(chaves))} for valor in valores]

print(resultado)

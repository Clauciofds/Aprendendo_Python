"""
Criando meu próprio versão de loop

iter([1, 2, 3, 4, 5])

iter("Clauc")



"""

def meu_for(interavel):
   it = iter(interavel)
   while True:
       try:
           print(next(it), end="-")
       except:
           print(f"\n")
           break

meu_for("Claucio")

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)
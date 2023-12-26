"""
Criando meu próprio versão de loop

iter([1, 2, 3, 4, 5])

iter("Clauc")



"""
def meu_for(interavel):
    it = iter(interavel)
    try:
        while True:
            print(next(it), end="-")
    except StopIteration:
        print()

meu_for("Claucio")


numeros = [1, 2, 3, 4, 5]

# meu_for(numeros)



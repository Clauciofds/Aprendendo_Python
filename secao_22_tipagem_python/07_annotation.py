import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = 'Claucio'

peso: float = 67.9
ativo: bool = True

print(__annotations__)

class Pessao:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessao(nome='Claucio', idade=37, peso=67.2)

print(p.__dict__)

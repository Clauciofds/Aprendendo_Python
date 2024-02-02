# nomes: list = ['Claucio', 'Cleiton']
#
# versoes: tuple = (3, 4, 8)
#
# opcoes: dict = {'ar': True, 'banco_couro': True}
#
# valores: set = {3, 4, 5, 6}
#
# print(nomes)
# print(versoes)
# print(opcoes)
# print(valores)
#
# print(__annotations__)

print('')

import random
from typing import List, Tuple, Set, Dict

# para inserir caracteres especiais basta clicar Windows+.
NAIPES: list = '♥️ ♦️ ♠️ ♣️'.split()
CARTAS: list = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_baralho(aleatoria: bool = False) -> BARALHO:
    """Cria um baralha com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatoria:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerancia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0:4], baralho[4:8], baralho[8:12], baralho[12:16])


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: BARALHO = criar_baralho(aleatoria=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

"""
POO - Classes

Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine a automação de lampadas de um sistema elétrico.

Classe podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No casa da lâmpada, possivelmente iriámos querer saer se a lâmpada
    é 110 ou 220 volts, se ele é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

    - Método (função) -> Representa os comportamentos do objeto. Ou seja as ações que este objeto pode realizar.
    No casa da lâmpada, ligar ou desligar.


--- OBSERVAÇÕES:
--- Por convenção nomeamos as classes com a primeiro letra maiúscala e em nome compostos sempre a primeiro
letra das palavras sempre iniciais maiúsculas.

--- Quando estamos planejando um software e definimos quais classes teremos que ter no sistem, chamamos estes
    objetos serão entidades.

"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()

print(type(lamp))


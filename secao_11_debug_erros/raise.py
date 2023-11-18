"""
Levantando os próprios erros com raise

raise -> Lança exceções

Obs: O raise não é uma função. É uma palavra reservada, assim como def ou qualque outra em Python.

Para simplificar, pense no raise como sendo útil para que possamo criar nossa próprias exceções e mensagens
de erro.

A forma gera de utilizaçao é:

raise TipoDoErro("Mensagem de erro")


"""
# Exemplo prático

def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")
    if type(texto) is not str:
        raise TypeError("texto precisa ser string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser um string")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser um entre: {cores}")
    print(f"O texto {texto} será impresso no cor {cor}")

colore("True", "azul")


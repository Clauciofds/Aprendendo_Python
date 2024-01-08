"""
O método repr é um método especial que define como um objeto é representado
 como uma string.
Ele é chamado automaticamente quando você usa a função repr() ou quando você
imprime um objeto sem usar a função print(). O objetivo do método repr é
retornar uma string que possa ser usada para recriar o objeto, se possível.
Por exemplo, se você tiver uma data chamada hoje, o método repr vai retornar
uma string como ‘datetime.date(2023, 12, 22)’, que você pode usar para criar
outra data igual.

O método repr é diferente do método str, que também retorna uma string que
representa um objeto, mas de uma forma mais amigável para o usuário final.
O método str é chamado quando você usa a função print() ou quando você converte
um objeto em uma string usando a função str(). Por exemplo, se você tiver uma
data chamada hoje, o método str vai retornar uma string como ‘22/12/2023’, que
é mais fácil de ler do que o método repr.

Você pode implementar o método repr em suas próprias classes, definindo como
você quer que seus objetos sejam representados como strings. Isso pode ser útil
para depurar ou testar o seu código. Você também pode implementar o método str
se você quiser personalizar a forma como seus objetos são mostrados para o usuário.

Um pequeno código como exemplo da representação de uma data qualquer usando o método repr seria:
"""

# Importando o módulo datetime
import datetime


# Criando uma classe para representar uma data
class MinhaData:
    # Construtor da classe, recebe ano, mês e dia como parâmetros
    def __init__(self, ano, mes, dia):
        # Atribuindo os valores aos atributos da classe
        self.ano = ano
        self.mes = mes
        self.dia = dia

    # Método __repr__ para retornar uma string que representa a data
    def __repr__(self):
        # Usando o método __repr__ da classe datetime.date para formatar a string
        return datetime.date(self.ano, self.mes, self.dia).__repr__()

    # Método __str__ para retornar uma string que mostra a data de forma amigável
    def __str__(self):
        # Usando o método strftime da classe datetime.date para formatar a string
        return datetime.date(self.ano, self.mes, self.dia).strftime("%d/%m/%Y")


# Testando o código
# Criando uma instância da classe MinhaData com a data de hoje
hoje = MinhaData(2023, 12, 22)

# Imprimindo a representação da data usando o método __repr__
print(repr(hoje))

# Imprimindo a representação da data usando o método __str__
print(hoje)

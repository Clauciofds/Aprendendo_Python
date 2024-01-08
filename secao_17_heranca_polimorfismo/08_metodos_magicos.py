"""
POO - Método Mágicos

    Métodos Mágicos, são todos os métodos que utilizam dunder.

- dunder init -> __init__()


"""
class Livro:
    def __init__(self, titulo, autor, paginas, data):
        self.titulo = titulo
        self.auto = autor
        self.paginas = paginas
        self.data = data

    def __repr__(self):
        return f'{self.titulo} escrito por {self.auto}'

    """
    def __str__(self):  # No código a função __str__ tem prioridade de execução
        return self.titulo
    """

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        """
        try:
            msg = ''
            for _ in range(other):
                msg += ' ' + str(self)
        except (NameError, TypeError) as err:
            print('O segundo atributo dever ser inteiro')

        """
        if isinstance(other, int):
            msg = ''
            for _ in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python', 'Geek', 400, '04/01/2024')
livro2 = Livro('IA', 'Geek' , 350, '04/02/2024')

print(livro1)
print(livro2)
print(f'{len(livro1)} páginas')

print(livro1 + livro2)
print(livro1 * 3)
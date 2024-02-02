# def cumprimento(nome: str) -> str:
#     return f'Olá, {nome}'
#
# print(cumprimento('Claucio'))

def header(text: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"\n{text.title()}\n{'-' * len(text)}\n"
    else:
        return f"  {text.title()}  ".center(40, '#')

print(header("claucio santos"))

print(header('cleiton', alinhamento=False))


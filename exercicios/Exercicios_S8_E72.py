# Definição da classe para representar um vetor tridimensional
class Vector:
    def __init__(self, x, y, z):
        self.x = x  # componente x
        self.y = y  # componente y
        self.z = z  # componente z

# Função para calcular a soma de dois vetores
def soma(v1, v2):
    resultado = Vector(0, 0, 0)  # Inicializa um vetor com todas as componentes como 0
    resultado.x = v1.x + v2.x  # Soma as componentes x
    resultado.y = v1.y + v2.y  # Soma as componentes y
    resultado.z = v1.z + v2.z  # Soma as componentes z
    return resultado  # Retorna o vetor resultante

# Exemplo de uso
v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(4.0, 5.0, 6.0)

# Chama a função soma para calcular a soma dos vetores
resultado = soma(v1, v2)

# Imprime o resultado
print("Resultado da soma dos vetores:")
print("x:", resultado.x)
print("y:", resultado.y)
print("z:", resultado.z)

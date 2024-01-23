"""
Teste em python são realizado com ferramentas especializadas

            Aplicação web
.......................................
        fronten e backend
---------------------------------------
       teste automatizados
---------------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no códigos existe;
    - Testes garantem que novos recursos da sua aplicação não quebrem (altere) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigigdos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam bus.

>> TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro:
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso_);
    - Então refatora o código para realizar a funcionalidade e teste novamente;
    - Uma vez que o teste passe, o recurso é considerado completo.

Estes estágios de desenvolvimento do TDD são quase como mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;


"""
class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} mia')

felix = Gato('Felix')

felix.miar()

print(felix.nome)
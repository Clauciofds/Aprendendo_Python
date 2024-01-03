"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de
andares no prédio. excluindo o térreo, capacidade do elevador, e quantos pessoas estão
presentes nele.

A classe deve também disponivilizar os seguintes métodos:
    > Inicializa: que deve receber como parâmetros a capacidade do elevador e o
      total de andares do préio (os elevadores sempre começão no térreo e vazio);
    > Entra: para acrescentar um pessoa no elevador (sõ deve acrescentar se ainda
      houver espaço);
    > Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
      dentro dele);
    > Sobe: para subir um andar (não deve subir se já estiver no última andar):
    > Desce: para descer um andar (não deve descer se já estiver no térreo;
    > Encapsular todos os atributos da classe (criar os métodos set e get).
"""

class Elevador:
    def __init__(self, sum_floors, elev_capacity):
        self._current_floor = 0  # Groundo floor
        self._sum_floors = sum_floors
        self._elev_capacity = elev_capacity
        self._current_occupation = 0

    def get_current_floor(self):
        return self._current_floor

    def set_current_floor(self, floor):
        if 0 <= floor <= self._sum_floors:
            self._current_floor = floor
        else:
            print('Invaid floor!!')

    def get_sum_floors(self):
        return self._sum_floors

    def set_sum_floors(self, sum_floors):
        if sum_floors >= 1:
            self._sum_floors = sum_floors
        else:
            print('Invalid number floor!!!')

    def get_capacity(self):
        return self._elev_capacity

    def set_capacity(self, capacity):
        if capacity >= 1:
            self._elev_capacity = capacity
        else:
            print('Capacity exceeded!!!')

    def get_occupation(self):
        return  self._current_occupation

    def set_occupation(self, current_occupation):
        if 0 <= current_occupation <= self._elev_capacity:
            self._current_occupation = current_occupation
        else:
            print('Invalid occupation!!!')

    def Initialize(self, sum_floors, elev_capacity):
        self.set_current_floor(0)
        self.set_sum_floors(sum_floors)
        self.set_capacity(elev_capacity)
        self.set_occupation(0)

    def enter(self, number_people):
        avialable_capacity = self._elev_capacity - self._current_occupation
        if number_people <= avialable_capacity:
            self._current_occupation += number_people
            print(f'{number_people:02} person(s) entered the elevator.')
        else:
            print('There is not enough space for all the people.')

    def exit(self, number_people):
        if number_people <= self._current_occupation:
            self._current_occupation -= number_people
            print(f'{number_people} person(s) exited the elevator.')
        else:
            print('The elevator is empty!')

    def go_up(self, number_floor):
        if self._current_floor < self._sum_floors:
            self._current_floor += number_floor
            print(f'Elevator went up to the {self._current_floor}º floor.')
        else:
            print('The elevator is already on the top floor!!!')

    def go_down(self, number_floor):
        if self._current_floor - number_floor > 0:
            self._current_floor -= number_floor
            print(f'The elevator went down {self._current_floor}º floor.')
        else:
            print('The elevator is already on the ground floor!!!')


def main():
    elev1 = Elevador(6, 10)
    elev1.Initialize(6, 10)
    elev1.enter(2)
    elev1.go_up(2)
    elev1.go_down(10)
    print(elev1.get_occupation())


if __name__ == '__main__':
    main()

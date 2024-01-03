"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o vulume
e trocar os canais da televisão.

    > O controle de volume permite aumentar ou diminui a potência do volume de
      som em uma unidade de cada vez;
    > O controle de canal tambem permite aumentar e diminuir o númerio do canal
      em uma unidade, porém, também possibilita trocar para um canal indicado;
    > Também devem existir métodos para consultar o valor do volume de som e o
      canal selecionado.
"""

class Television:
    def __init__(self):
        self._volume = 5
        self._channel = 1

    def view_status(self):
        print(f'\nVolume {self._volume:02}{" ":<10}Channel {self._channel:02}')

    def volume_up(self):
        if self._volume > 100:
            self._volume += 1
            print(f'Volume {self._volume:02}{" ":<10}Channel {self._channel:02}')
        else:
            print(f'\n{"Max":<19}Channel {self._channel:02}')

    def volume_down(self):
        if self._volume > 0:
            self._volume -= 1
            print(f'\nVolume {self._volume:02}{"":10}Channel {self._channel:02}')
        else:
            print(f'\n{"Mute":<19}Channel {self._channel:02}')

    def channel_up(self):
        if self._channel < 50:
            self._channel += 1
            print(f'\nVolume {self._volume:02}{"":<10}Channel {self._channel:02}')
        else:
            self._channel = 0
            print(f'\nVolume {self._volume:02}{"":<10}Channel {self._channel:02}')

    def channel_down(self):
        if self._channel > 0:
            self._channel -= 1
            print(f'\nVolume {self._volume:02}{"":<10}Channel {self._channel:02}')
        else:
            self._channel = 50
            print(f'\nVolume {self._volume:02}{"":10}Channel {self._channel:02}')

    def set_volume(self, value):
        if 1 <= value < 100:
            self._volume = value
            print(f'\nVolume {self._volume:02}{"":<10}Channel {self._channel:02}')
        elif value == 100:
            print(f'\n{"Volume Max":<19}Channel {self._channel:02}')
        elif value == 0:
            print(f'\n{"Mute":<19}Channel {self._channel:02}')

    def set_channel(self, value):
        if 0 <= value <= 50:
            self._channel = value
            print(f'\nVolume {self._volume:02}{"":<10}Channel {self._channel:02}')


class RemoteControl:
    def __init__(self, television):
        self.television = television

    def volume_up(self):
        self.television.volume_up()

    def volume_down(self):
        self.television.volume_down()

    def channel_up(self):
        self.television.channel_up()

    def channel_down(self):
        self.television.channel_down()

    def set_volume(self, value):
        self.television.set_volume(value)

    def set_channel(self, value):
        self.television.set_channel(value)


def main():
    lg = Television()
    remote_control = RemoteControl(lg)

    remote_control.channel_up()

    remote_control.volume_down()

    remote_control.set_channel(48)

    remote_control.volume_down()

    remote_control.set_volume(0)


if __name__ == '__main__':
    main()
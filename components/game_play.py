import time

from ursina import held_keys

from components.fado import Fado

up = 'w'
down = 's'
left = 'a'
right = 'd'


class GamePlay:
    def __init__(self, game_state):
        self.state = game_state
        self.fado = Fado(self.state)
        self.bloked = True

    def start_game(self):
        self.bloked = False

    def handle_keys(self):
        if not self.bloked:
            self.move_fado()

    def move_fado(self):
        if held_keys[up]:
            self.fado.position += (0, time.dt, 0)
        if held_keys[down]:
            self.fado.position -= (0, time.dt, 0)
        if held_keys[right]:
            self.fado.position += (time.dt, 0, 0)
        if held_keys[left]:
            self.fado.position -= (time.dt, 0, 0)

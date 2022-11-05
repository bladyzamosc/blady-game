from components.fado import Fado
from components.obstacles import Obstacles


class GamePlay:
    def __init__(self):
        self.fado = Fado()
        self.obstacles = Obstacles()
        self.fado.visible = False
        self.blocked = True
        self.counter = 0

    def pause(self):
        self.blocked = True

    def resume(self):
        self.blocked = False
        self.fado.visible = True

    def save(self):
        print("save")

    def update_game_play(self):
        if not self.blocked:
            self.counter += 1
            self.obstacles.update_obstacles(counter=self.counter)
            self.fado.update_fado()


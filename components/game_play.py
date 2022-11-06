from components.fado import Fado
from components.game_stats import GameStats
from components.obstacles import Obstacles


class GamePlay:
    def __init__(self):
        self.fado = Fado()
        self.obstacles = Obstacles()
        self.game_stats = GameStats()
        self.fado.visible = False
        self.blocked = True

    def pause(self):
        self.blocked = True

    def resume(self):
        self.blocked = False
        self.fado.visible = True

    def save(self):
        print("save")

    def update_game_play(self):
        if not self.blocked:
            self.game_stats.update_counter()
            self.obstacles.update_obstacles(game_stats=self.game_stats, fado=self.fado)
            self.fado.update_fado()


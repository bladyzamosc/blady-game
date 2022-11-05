from components.fado import Fado


class GamePlay:
    def __init__(self):
        self.fado = Fado()
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
            self.fado.update_fado()


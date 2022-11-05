from ursina import camera, Entity

FACTOR = 0.07


class Fado(Entity):

    def __init__(self, game_state):
        super().__init__(
            parent=camera.ui,
            model='cube'
        )
        self.game_state = game_state
        self.visible = True
        self.texture = 'assets/dog.png'
        self.scale = (FACTOR, FACTOR, FACTOR)
        self.position = (-0.80, 0, 0)


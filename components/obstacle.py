import random

from ursina import Entity, camera, window


class Obstacle(Entity):

    def __init__(self, asset, factor, move):
        super().__init__(
            parent=camera.ui,
            model='cube'
        )
        self.visible = True
        self.texture = 'assets/' + asset
        self.scale = (factor, factor, factor)
        self.position = (window.bottom_right.x, random.uniform(window.bottom_right.y, window.top_right.y), 0)
        self.move = move

    def move_position(self):
        self.position -= (self.move.delta_x, self.move.delta_y, 0)

    def is_out_of_window(self):
        return window.left.x > self.position.x

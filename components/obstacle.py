import random

from ursina import Entity, camera, window

from components.const import NEGATIVE


class Obstacle(Entity):

    def __init__(self, type_of_obstacle, factor, move):
        super().__init__(
            parent=camera.ui,
            model='cube'
        )
        self.visible = True
        self.texture = self.asset_by_type(type_of_obstacle)
        self.scale = (factor, factor, factor)
        self.position = (window.bottom_right.x, random.uniform(window.bottom_right.y, window.top_right.y), 0)
        self.move = move
        self.collider = 'box'
        self.type_of_obstacle = type_of_obstacle

    def move_position(self):
        self.position -= (self.move.delta_x, self.move.delta_y, 0)

    def is_out_of_window(self):
        return window.left.x > self.position.x

    def asset_by_type(self, type_of_obstacle):
        result = 'assets/'
        if type_of_obstacle == NEGATIVE:
            return result + 'negative.png'
        return result + 'positive.png'

import time

from ursina import camera, Entity, held_keys, window, Animation

from components.const import UP, DOWN, RIGHT, LEFT

FACTOR = 0.07


class Fado(Entity):

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube'
        )
        self.visible = True
        self.texture = 'assets/labrador.png'
        self.scale = (FACTOR, FACTOR, FACTOR)
        self.position = (-0.80, 0, 0)
        self.collider = 'box'


    def update_fado(self):
        self.react_key()
        self.ensure_position()

    def react_key(self):
        if held_keys[UP]:
            self.position += (0, time.dt, 0)
        if held_keys[DOWN]:
            self.position -= (0, time.dt, 0)
        if held_keys[RIGHT]:
            self.position += (time.dt, 0, 0)
        if held_keys[LEFT]:
            self.position -= (time.dt, 0, 0)

    def ensure_position(self):
        x = self.position.x
        y = self.position.y

        if x > window.bottom_right.x:
            self.position = (window.bottom_right.x, y, 0)
        if y < window.bottom_right.y:
            self.position = (x, window.bottom_right.y, 0)
        if x < window.top_left.x:
            self.position = (window.top_left.x, y, 0)
        if y > window.top_left.y:
            self.position = (x, window.top_left.y, 0)

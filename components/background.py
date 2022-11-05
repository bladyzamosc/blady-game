from ursina import Entity


class Background:
    def setup(self):
        Entity(model='quad', scale=(20,10), texture='assets/background.png')

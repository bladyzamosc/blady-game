from random import random, uniform

MIN_Y = 0.02

MAX_Y = 0.01

MAX = 0.015

MIN = 0.005


class Move:
    def __init__(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y

    @staticmethod
    def random_move(straight=True, base=0.0):
        x = uniform(MIN, MAX) + base
        if straight:
            y = 0
        else:
            y = uniform(MIN_Y, MAX_Y) + base
        return Move(x, y)

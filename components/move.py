from random import random, uniform

MIN_Y = 0.02

MAX_Y = 0.01

MAX = 0.05

MIN = 0.01


class Move:
    def __init__(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y

    @staticmethod
    def random_move(straight=True):
        x = uniform(MIN, MAX)
        if straight:
            y = 0
        else:
            y = uniform(MIN_Y, MAX_Y)
        return Move(x, y)

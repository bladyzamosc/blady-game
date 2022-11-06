from random import choice, uniform

from ursina import destroy, distance

from components.const import NEGATIVE, POSITIVE
from components.move import Move
from components.obstacle import Obstacle

DESTROY_DELAY = 0.2

MULTIPLICATOR = 10
MULTIPLICATOR_POSITIVE = 100
LEVEL_MULTIPLICATOR = 1000
LEVEL_BASE = 0.005
MAX = 0.09
MIN = 0.02


class Obstacles:

    def __init__(self):
        self.elements = []

    def update_obstacles(self, game_stats, fado):
        self.generate_obstacles(game_stats.counter, NEGATIVE, MULTIPLICATOR)
        self.generate_obstacles(game_stats.counter, POSITIVE, MULTIPLICATOR_POSITIVE)
        self.manage_obstacles(game_stats, fado)
        print(game_stats.counter, "  ", game_stats.score, "  ", game_stats.lives)

    def generate_obstacles(self, counter, type, factor):
        generate = choice([True, False])
        base = self.determine_base(counter)
        if generate and counter % factor == 0:
            m = Move.random_move(straight=True, base=base)
            o = Obstacle(type, uniform(MIN, MAX), m)
            self.elements.append(o)

    def manage_obstacles(self, game_stats, fado):
        for o in self.elements:
            self.handle_collision(game_stats, o, fado)
            o.move_position()
            if o.is_out_of_window():
                game_stats.update_score(1)
                self.handle_destroyed_obstacle(o)

    def handle_destroyed_obstacle(self, o):
        self.elements.remove(o)
        destroy(o, DESTROY_DELAY)

    def determine_base(self, counter):
        return (counter / LEVEL_MULTIPLICATOR) * LEVEL_BASE

    def handle_collision(self, game_stats, o, fado):
        interacts = fado.intersects(o)
        if interacts.hit:
            if o.type_of_obstacle == NEGATIVE:
                game_stats.update_lives(-1)
            else:
                game_stats.update_lives(1)
            self.handle_destroyed_obstacle(o)

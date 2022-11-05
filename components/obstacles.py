from random import choice, uniform

from ursina import destroy

from components.move import Move
from components.obstacle import Obstacle

STEP = 10

MAX = 0.09

MIN = 0.01


class Obstacles:
    def __init__(self):
        self.obstacles = []

    def update_obstacles(self, counter):
        self.generate_obstacles(counter)
        self.manage_obstacles()

    def generate_obstacles(self, counter):
        generate = choice([True, False])
        if generate and counter % STEP == 0:
            m = Move.random_move(True)
            o = Obstacle('dog.png', uniform(MIN, MAX), m)
            self.obstacles.append(o)
        print(counter)

    def manage_obstacles(self):
        for o in self.obstacles:
            o.move_position()
            if o.is_out_of_window():
                self.obstacles.remove(o)
                destroy(o, 1)

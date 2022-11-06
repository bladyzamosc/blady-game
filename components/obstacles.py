from random import choice, uniform

from ursina import destroy, distance

from components.move import Move
from components.obstacle import Obstacle

DESTROY_DELAY = 0.2

MULTIPLICATOR = 10

LEVEL_MULTIPLICATOR = 1000

LEVEL_BASE = 0.005

MAX = 0.09

MIN = 0.02


class Obstacles:
    def __init__(self):
        self.obstacles = []

    def update_obstacles(self, game_stats, fado):
        self.generate_obstacles(game_stats.counter)
        self.manage_obstacles(game_stats, fado)
        print(game_stats.counter, "  ", game_stats.score, "  ", game_stats.lives)

    def generate_obstacles(self, counter):
        generate = choice([True, False])
        base = self.determine_base(counter)
        if generate and counter % MULTIPLICATOR == 0:
            m = Move.random_move(straight=True, base=base)
            o = Obstacle('dog.png', uniform(MIN, MAX), m)
            self.obstacles.append(o)

    def manage_obstacles(self, game_stats, fado):
        for o in self.obstacles:
            self.handle_collision(game_stats, o, fado)
            o.move_position()
            if o.is_out_of_window():
                game_stats.update_score(1)
                self.handle_destroyed_obstacle(o)

    def handle_destroyed_obstacle(self, o):
        self.obstacles.remove(o)
        destroy(o, DESTROY_DELAY) 

    def determine_base(self, counter):
        return (counter / LEVEL_MULTIPLICATOR) * LEVEL_BASE

    def handle_collision(self,game_stats, o, fado):
        interacts = fado.intersects(o)
        print(interacts.hit,"/", interacts.distance, "/")
        if interacts.hit:
            game_stats.update_lives(-1)
            self.handle_destroyed_obstacle(o)

            

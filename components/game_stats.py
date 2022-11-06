from components.const import MAX_LIVES, INITIAL_LIVES


class GameStats:
    def __init__(self):
        self.score = 0
        self.counter = 0
        self.lives = INITIAL_LIVES

    def update_counter(self):
        self.counter += 1

    def update_score(self, number):
        self.score += number;

    def update_lives(self, number):
        self.lives += number
        if self.lives > MAX_LIVES:
            self.lives = MAX_LIVES

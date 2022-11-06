from ursina import color, Text
from ursina.prefabs.health_bar import HealthBar

from components.const import MAX_LIVES


class GameScore:
    def __init__(self, game_play):
        self.game_play = game_play
        self.health_bar = HealthBar(bar_color=color.gold.tint(-.25), roundness=.2, max_value=MAX_LIVES)
        self.health_bar.value = self.game_play.game_stats.lives

        self.score = Text(text='Score: 0',color=color.gold)
        self.score.default_resolution = 1080 * Text.size
        self.score.scale = 1
        self.score.position=(0, .45)
        self.score.background=color.black

    def update_score(self):
        self.score.text = 'Score: '+ str(self.game_play.game_stats.score)
        if self.health_bar.value != self.game_play.game_stats.lives:
            self.health_bar.value = self.game_play.game_stats.lives

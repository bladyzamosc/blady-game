from ursina import *

from components.background import Background
from components.const import PAUSE
from components.game_play import GamePlay
from components.game_score import GameScore
from components.game_window import GameWindow
from components.menu import Menu
from components.menu_button import MenuButton
from components.splash import Splash

global game_state
global game_window


def setup_controls():
    Splash.splash()
    background = Background()
    background.setup()


def handle_keys():
    if held_keys[PAUSE]:
        menu.switch()


def update():
    handle_keys()
    if not game_play.is_game_over():
        game_play.update_game_play()
        game_score.update_score()
    else:
        Splash.game_over(game_play.game_stats.score)
        menu.switch(False)
        game_play.destroy_elements()


# Start
game_window = GameWindow()
app = Ursina()

game_play = GamePlay()
game_score = GameScore(game_play)
setup_controls()
game_window.setup()
menu = Menu(game_play)
menuButton = MenuButton(menu)
app.run()

from ursina import Ursina, held_keys

from components.background import Background
from components.game_play import GamePlay
from components.game_window import GameWindow
from components.menu import Menu
from components.menu_button import MenuButton
from components.splash import Splash
from components.util import pause

global game_state
global game_window


def setup_controls(game_window, game_play):
    Splash.splash()
    background = Background()
    background.setup()


def pre_app_setup():
    game_window = GameWindow()
    return game_window


def handle_keys():
    if held_keys[pause]:
        menu.switch()


def update():
    handle_keys()
    game_play.update_game_play()


# Start
game_window = pre_app_setup()
app = Ursina()
game_play = GamePlay()
setup_controls(game_window, game_play)
game_window.setup()
menu = Menu(game_play)
menu.setup()
menuButton = MenuButton(menu)
app.run()

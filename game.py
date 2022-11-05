from ursina import Ursina, held_keys

from components.background import Background
from components.game_play import GamePlay
from components.game_state import GameState
from components.game_window import GameWindow
from components.menu import Menu
from components.menu_button import MenuButton
from components.splash import Splash

global game_state
global game_window


def setup_controls(game_window):
    Splash.splash()
    background = Background()
    background.setup()
    game_state = GameState()
    game_window.setup()
    menu = Menu(game_state)
    menu.setup()
    menuButton = MenuButton(menu)
    return game_state


def pre_app_setup():
    game_window = GameWindow()
    return game_window


def setup_gameplay(game_state):
    game_play = GamePlay(game_state=game_state)
    game_play.start_game()
    return game_play


def update():
    game_play.handle_keys()

# Start
game_window = pre_app_setup()
app = Ursina()
game_state = setup_controls(game_window)
game_play = setup_gameplay(game_state)
app.run()

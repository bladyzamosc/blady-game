from ursina.prefabs.button import *
from ursina import *
from components.game_window import GameWindow
from components.menu.menu_button import MenuButton

GameWindow.setup_window()
app = Ursina()
GameWindow.setup_window_post_ursina()

m = MenuButton()

app.run()  # opens a window and starts the game.

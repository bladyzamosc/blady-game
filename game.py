from ursina import Ursina

from components.background import Background
from components.game_state import GameState
from components.game_window import GameWindow
from components.menu.menu import Menu
from components.menu.menu_button import MenuButton

game_window = GameWindow()
app = Ursina()

background = Background()
background.setup()

game_state = GameState()
game_window.setup()

menu = Menu(game_state)
menu.setup()
menuButton = MenuButton(menu)

app.run()  # opens a window and starts the game.

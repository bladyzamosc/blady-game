from ursina import *

from components.menu.menu import Menu

menu = Menu()


def show_menu():
    menu.visible = not menu.visible


class MenuButton(Entity):
    def __init__(self):
        self.parent = camera.ui
        menu_button = Button(color=color.dark_gray, scale=.05, text_origin=(-.5, 0))
        menu_button.on_click = show_menu
        menu_button.position = (0.85, 0.45, 0)

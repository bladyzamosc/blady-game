from ursina import Entity, camera, Button

from components.const import MENU_BUTTON_COLOR, MENU_TEXTURE_COLOR


class MenuButton(Entity):

    def __init__(self, menu):
        self.parent = camera.ui
        self.menu = menu
        menu_button = Button(color=MENU_BUTTON_COLOR, scale_y=.05, scale_x=.1)
        menu_button.on_click = self.show_hide_menu
        menu_button.position = (0.83, 0.45, 0)
        menu_button.text='Menu'
        menu_button.text_entity.color=MENU_TEXTURE_COLOR

    def show_hide_menu(self):
        self.menu.switch()

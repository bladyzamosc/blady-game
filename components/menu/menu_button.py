from ursina import Entity, camera, color, Button


class MenuButton(Entity):

    def __init__(self, menu):
        self.parent = camera.ui
        self.menu = menu
        menu_button = Button(color=color.dark_gray, scale=.05, text_origin=(-.5, 0), icon = 'cog')
        menu_button.on_click = self.show_menu
        menu_button.position = (0.85, 0.45, 0)

    def show_menu(self):
        self.menu.change_visibility()

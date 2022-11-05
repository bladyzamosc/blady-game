from ursina import Entity, color, camera, Button, application

from components.const import MENU_BUTTON_COLOR, MENU_BACKGROUND_COLOR, MENU_TEXTURE_COLOR

ORIGIN_ONE = -0.2

SCALE_Y = 0.5

SCALE_X = 4.9


class Menu(Entity):

    def __init__(self, game_state, visible=False):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(1 / 2, 1 / 2),
            origin=(-.0, .0),
            position=(-.0, .0),
            texture_scale=(5, 8),
            color=MENU_BACKGROUND_COLOR
        )
        self.game_state = game_state
        self.visible = visible
        self.item_parent = Entity(parent=self, scale=(1 / 5, 1 / 5))

    def setup(self):
        origin_two = -1.5
        right = 1
        resume = self.create_button(right, origin_two, "Resume")
        resume.on_click = self.change_visibility
        origin_two += 0.1
        right -= 0.5
        about = self.create_button(right, origin_two, "About")
        origin_two += 0.6
        right -= 3
        exit_b = self.create_button(right, origin_two, "Exit")
        exit_b.on_click = self.quit

    def create_button(self, right, origin_two, text):
        b = Button(
            parent=self.item_parent,
            model='quad',
            scale_x=SCALE_X,
            scale_y=SCALE_Y,
            origin=(ORIGIN_ONE, origin_two),
            z=-.01
        )
        b.position = (-1, right)
        b.color = MENU_BUTTON_COLOR
        b.text = text
        b.text_entity.color=MENU_TEXTURE_COLOR
        return b

    def change_visibility(self):
        if self.visible:
            self.game_state.resume()
        else:
            self.game_state.pause()
        self.visible = not self.visible

    def quit(self):
        self.game_state.save()
        application.quit()

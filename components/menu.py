from ursina import Entity, camera, Button, application, Text, destroy

from components.const import MENU_BUTTON_COLOR, MENU_BACKGROUND_COLOR, MENU_TEXTURE_COLOR, DELAY, GOLD

ORIGIN_ONE = -0.2

SCALE_Y = 0.5

SCALE_X = 4.9


class Menu(Entity):

    def __init__(self, game_play):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(1 / 2, 1 / 2),
            origin=(-.0, .0),
            position=(-.0, .0),
            texture_scale=(5, 8),
            color=MENU_BACKGROUND_COLOR
        )
        self.game_play = game_play
        self.set_visible(False)
        self.item_parent = Entity(parent=self, scale=(1 / 5, 1 / 5))
        self.setup()

    def setup(self):
        origin_two = -1.5
        right = 1
        self.start_b = self.create_button(right, origin_two, "Start new")
        self.start_b.on_click = self.start_new_game
        origin_two += 0.1
        right -= 0.5
        self.resume = self.create_button(right, origin_two, "Resume")
        self.resume.on_click = self.switch
        self.resume.enabled = False
        origin_two += 0.1
        right -= 0.5
        self.about = self.create_button(right, origin_two, "About")
        self.about.on_click = self.about_clicked
        origin_two += 0.5
        right -= 2.5
        self.exit_b = self.create_button(right, origin_two, "Exit")
        self.exit_b.on_click = self.quit

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
        b.text_entity.color = MENU_TEXTURE_COLOR
        return b

    def switch(self, resume_enabled=True):
        if self.visible:
            self.game_play.resume()
        else:
            self.game_play.pause()
        self.set_visible(not self.visible)
        self.resume.enabled = resume_enabled

    def set_visible(self, flag):
        self.visible = flag
        self.enabled = flag

    def start_new_game(self):
        self.game_play.destroy_elements()
        self.switch()

    def quit(self):
        application.quit()

    def about_clicked(self):
        Text.default_resolution = 1080 * Text.size
        text1 = Text(text="Description: The very first program in Python", scale=1, world_z=camera.overlay.z - 1,
                     color=GOLD, position=(-0.8, -0.35, 0))
        destroy(text1, delay=DELAY)
        text2 = Text(text="Email: bladyzamosc@gmail.com", scale=1, world_z=camera.overlay.z - 1, color=GOLD,
                     position=(-0.8, -0.3, 0))
        destroy(text2, delay=DELAY)

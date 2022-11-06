from ursina import camera, color, Sprite, destroy, curve, Text

from components.const import MENU_BACKGROUND_COLOR, MENU_TEXTURE_COLOR

DELAY = 4


class Splash:

    @staticmethod
    def splash():
        camera.overlay.color = MENU_BACKGROUND_COLOR
        logo = Sprite(name='blady-game', parent=camera.ui, texture='assets/dog.png', world_z=camera.overlay.z - 2,
                      scale=.15, color=color.clear)
        logo.animate_color(MENU_TEXTURE_COLOR, duration=2, delay=1, curve=curve.out_quint_boomerang)

        Text.default_resolution = 1080 * Text.size
        text = Text(text="Blady Game")
        text.position = (-0.15, 0.4, 0)
        text.scale = 2
        text.world_z = camera.overlay.z - 1

        camera.overlay.animate_color(color.clear, duration=1, delay=2)
        destroy(text, delay=DELAY - 1)
        destroy(logo, delay=DELAY)

        def splash_input(key):
            destroy(logo)
            destroy(text)
            camera.overlay.animate_color(color.clear, duration=.25)

        logo.input = splash_input
        text.input = splash_input

    @staticmethod
    def game_over(number):
        Text.default_resolution = 1080 * Text.size
        text = Text(text="Game over. Your score: " + str(number))
        text.position = (-0.30, 0.4, 0)
        text.scale = 2
        text.world_z = camera.overlay.z - 1
        destroy(text, delay=DELAY - 1)
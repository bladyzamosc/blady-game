import os

from ursina import window, color

from components.util import Util


class GameWindow:
    def __init__(self):
        window.title = 'Blady game'
        window.borderless = False
        window.fullscreen = False
        window.icon_filename = Util.path_to_asset('game.ico')

    def setup(self):
        window.exit_button.visible = False
        window.fps_counter.enabled = True
        window.color = color.light_gray

import os

from ursina import window, color

from components.util import Util


class GameWindow:
    def __init__(self):
        window.borderless = False
        window.fullscreen = False

    def setup(self):
        window.exit_button.visible = False
        window.fps_counter.enabled = True
        window.color = color.light_gray

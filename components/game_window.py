import os

from ursina import window, color

from components.util import Util


class GameWindow:

    @staticmethod
    def setup_window():
        window.title = 'Blady game'
        window.borderless = False
        window.fullscreen = False
        window.icon_filename = Util.path_to_asset('game.ico')

    @staticmethod
    def setup_window_post_ursina():
        window.exit_button.visible = False
        window.fps_counter.enabled = True
        window.color = color.light_gray

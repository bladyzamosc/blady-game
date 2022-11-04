from ursina import Entity, color, camera, Button, application, Tooltip


class Menu(Entity):
    color = color.olive

    def __init__(self, visible=False):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(4, 5.0),
            origin=(-.0, .0),
            position=(-.3, .4),
            texture_scale=(5, 8),
            color=color.dark_gray
        )
        self.visible=visible

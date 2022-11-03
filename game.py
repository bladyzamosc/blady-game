from ursina import *

app = Ursina()

window.title = 'BladyGame'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

cube = Entity(model='cube', color=color.azure, scale=(1, 3, 2))
random_generator = random.Random()


def update():
    rotate(cube)
    moveCamera()


def moveCamera():
    if held_keys['q']:
        camera.position += (0, time.dt, 0)
    if held_keys['a']:
        camera.position -= (0, time.dt, 0)


def input(key):
    if key == 'space':
        change_color(cube)


def change_color(obj):
    red = random_generator.random() * 255
    green = random_generator.random() * 255
    blue = random_generator.random() * 255
    obj.color = color.rgb(red, green, blue)


def rotate(obj):
    obj.rotation_y += time.dt * 100
    obj.rotation_z += time.dt * 50
    obj.rotation_x += time.dt * 75


app.run()

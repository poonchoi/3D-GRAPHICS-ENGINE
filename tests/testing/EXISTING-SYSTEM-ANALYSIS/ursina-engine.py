# import library
from ursina import *

# create an instance of the engine
app = Ursina()

# create an instance of entity class and specify shape
box = Entity(model='cube', color=color.red)

# function that calls itself every  frame
def update():
    # changes box position based on key input
    box.x -= held_keys['d'] * time.dt
    box.x += held_keys['a'] * time.dt
    box.z -= held_keys['w'] * time.dt
    box.z += held_keys['s'] * time.dt

    # rotates box every frame
    theta = 100 * time.dt
    box.rotation_z += theta
    box.rotation_x += theta

# calls the ursina run function which runs the program
app.run()
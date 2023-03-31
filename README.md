# PG3D

PG3D is a simple 3D graphics library written using Pygame.


## Installation
---
1) Install Python 3.7 or newer. https://www.python.org/downloads/
2) Open cmd/terminal and type:
```
pip install pg3d
```

## Dependencies
---
* python 3.7+
* pygame

## Usage
---
1) Import the library
```py
from pg3d import *
```
2) Create an App instance and call the run function
```py
app = App()

#---Code goes here---#

#--------------------#

app.run()
```

## API Reference
---
```py
App(kwargs):


kwargs:
    dimensions=(1000, 700)
    cam_pos=[0, 0, 0]
    BG_COLOR=None
    LINE_COLOR=None
    VERTEX_SIZE=2              
    fullscreen=False           
    mouse_look=False  # Use mouse for camera orientation


functions:
    run()  # Draws all vertices and checks for movement
```
---
```py
Model(args)


args:
    app   # Specify the App() object
    path  # Specify path of .obj file
```
---
```py
Pyramid(args, kwargs)


args:
    app  # Specify the App() object


kwargs:
    size=1
    center=[0, 0, 0]
```
---
```py
Cube(args, kwargs)


args:
    app  # Specify the App() object


kwargs:
    size=1
    center=[0, 0, 0]
```
---
```py
Tetrahedron(args, kwargs)


args:
    app  # Specify the App() object


kwargs:
    size=1
    center=[0, 0, 0]
```
---
```py
Triangle(args)


args:
    app       # Specify the App() object
    vertices  # List or tuple with 3 cartesian coordinates


functions:
    __getitem__(index)  # Returnes indext point of Triangle object
```
---
```py
Point(args, kwargs)


args:
    app         # Specify the App() object
    coordinate  # A list with a single cartesian coordinate


kwargs:
    vertex=True  # If true the point is drawn and vice versa


functions:
    __repr__()                 # Prints Point object
    __setitem__(index, value)  # Sets indexed coordinate of Point object to value
    __getitem__(index)         # Returns indexed coordinate of Point object
```
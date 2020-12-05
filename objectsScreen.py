from objects import *

base = Rectangle(False, {
        'width': '50%',
        'height': '70%',
        'x': '25px',
        'y': '20px',
        'color': color(80,0,0),
        'border': '5px',
        'radius': '5px'
    })

def settings():
    size(screenSize['x'], screenSize['y'])

def setup():
    pass

def draw():
    base.draw()
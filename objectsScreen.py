from objects import *

Alpha = Rectangle(False, {
        'width': '500px',
        'height': '500px',
        'x': '25px',
        'y': '20px',
        'background-color': color(0,0,80),
        'border': '1px',
        'radius': '0px'
    })

Beta = Rectangle(Alpha, {
        'width': '50%',
        'height': '100%',
        'background-color': color(255,0,0),
        'inherit': 'relative',
        'x': '0px',
        'y': '0px',
        'border': '0px'
    })

Charlie = Rectangle(Beta, {
        'width': '50%',
        'height': '100%',
        'background-color': color(0,255,0),
        'inherit': 'relative',
        'x': '0px',
        'y': '0px',
        'border': '0px'
    })

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    pass

def draw():
    Alpha.draw()
    Beta.draw()
    Charlie.draw()
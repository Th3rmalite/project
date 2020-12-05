from objects import *

rectangle = Rectangle({
        'width': '50%',
        'height': '70%',
        'x': '25px',
        'y': '20px',
        'color': color(80,0,0),
        'border': '15px 10px 25px 0px'
    })

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    global rectangle
    print(rectangle.attribute.get)

def draw():
    rectangle.draw()
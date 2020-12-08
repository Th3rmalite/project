from objects import *

Background = Rectangle(False, {
    'width': '100%',
    'height': '100%',
    'background-color': color(255,255,255),
    'border': '0px'
})

Table = Rectangle(False, {
    'rect-align': CENTER,
    'width': '40%',
    'height': '80%',
    'background-color': color(218, 214, 214),
    'x': '50%',
    'y': '50%',
    'border': '0px',
    'box-shadow': '5px 5px 3px'
})

Row1 = Rectangle(Table, {
    'rect-align': CORNER,
    'inherit': 'relative',
    'width': '100%',
    'height': '25%',
    'x': '0px',
    'y': '75%',
    'border': '0px',
    'box-shadow': '0px 5px 5px',
    'background-color': color(146, 191, 177)
})

Row2 = Rectangle(Table, {
    'rect-align': CORNER,
    'inherit': 'relative',
    'width': '100%',
    'height': '25%',
    'x': '0px',
    'y': '50%',
    'border': '0px',
    'box-shadow': '0px 5px 5px',
    'background-color': color(244, 172, 69)
})

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    pass
    
def draw():
    for index in range(len(content)):
        content[index].drawShadow()
        content[index].draw()
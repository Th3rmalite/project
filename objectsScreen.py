from objects import *
import time

# Definieer alle objecten in een scherm. Je kan deze dupliceren en aanpassen. 
# Hier kan je ook aanpassen wat er gebeurt als je ergens overheen gaat met je muis.

def settings():
    size(screen['w'][0], screen['h'][0])

def setup():
    # In namenScherm.py
    global namenScherm
    namenScherm = Screen('namen', {})
    namenScherm.start()
    a = Rectangle(None, {
        'x': '150',
        'y': '250',
        'w': '500',
        'h': '300',
        'rectMode': CORNER
    })

    b = Button(a, {
        'x': '0',
        'y': '0',
        'fill': '255 0 100 255',
        'rectMode': CORNER
    })
    b.hover.setItems({
        'fill': '255 100 10 255'
    })
    b.selected.setItems({
        'fill': '0 255 0 255'
    })

    namenScherm.addData(namenScherm.name, {'appeltaart': 'dat is lekker'})
    namenScherm.stop()

def draw():
    for i in range(len(namenScherm.content)):
        namenScherm.content[i].draw()

def mousePressed():
    for i in range(len(namenScherm.content)):
        if namenScherm.content[i].isHover():
            namenScherm.content[i].mousePressedEvent()

def mouseReleased():
    for i in range(len(namenScherm.content)):
        namenScherm.content[i].mouseReleasedEvent()

setup()
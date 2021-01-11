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
        'x': '50%',
        'y': '50%',
        'w': '500',
        'h': '200',
        'rectMode': CENTER,
        'fill': '220 220 220 255',
        'stroke': 'None'
    })

    b = TextField(a, {
        'x': '50%',
        'y': '50%',
        'w': '170',
        'h': '40',
        'rectMode': CORNER,
        'stroke': '50 50 50',
        'strokeWeight': '3',
        'placeholder': 'Naam',
        'textSize': '18',
        'textAlign': [LEFT, CENTER],
        'radius': '5',
        'textMargin': '5 0'
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
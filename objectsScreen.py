from objects import *
import time

# Definieer alle objecten in een scherm. Je kan deze dupliceren en aanpassen. 
# Hier kan je ook aanpassen wat er gebeurt als je ergens overheen gaat met je muis.

def settings():
    size(screen['w'], screen['h'])

def setup():
    # In namenScherm.py
    global namenScherm
    namenScherm = Screen('namen', {})
    namenScherm.start()
    a = Button(None, {
        'x': 50,
        'y': 50
    })
    b = Button(None, {
        'x': 100,
        'y': 50
    })
    namenScherm.addData(namenScherm.name, {'appeltaart': 'dat is lekker'})
    namenScherm.stop()

def draw():
    for i in range(len(namenScherm.content)):
        namenScherm.content[i].draw()
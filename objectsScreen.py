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
    global test
    test = Rectangle(None, {
        'fill': '255 0 0 0'
    })
    print(test.properties.getItems())
    namenScherm.addData(namenScherm.name, {'appeltaart': 'dat is lekker'})
    namenScherm.stop()

def draw():
    test.draw()
from objects import *
import time

# Definieer alle objecten in een scherm. Je kan deze dupliceren en aanpassen. 
# Hier kan je ook aanpassen wat er gebeurt als je ergens overheen gaat met je muis.

def settings():
    size(screen['w'], screen['h'])

def setup():
    # In namenScherm.py
    namenScherm = Screen('namen', {})
    namenScherm.start()
    test = Instance(None, {})
    print(test.properties.getProperties())
    namenScherm.addData(namenScherm.name, {'appeltaart': 'dat is lekker'})
    namenScherm.stop()

    # In objectsScreen.py
    puntenScherm = Screen('punten', {})
    puntenScherm.start()

    puntenScherm.addData(puntenScherm.name, namenScherm.data)
    puntenScherm.stop()

    # In main.py
    print(namenScherm.getData(), puntenScherm.getData())

def draw():
    pass

setup()
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
    test = FormObject(None,{
        'w': '50%',
        'h': '10%',
    })
    global test
    namenScherm.addData(namenScherm.name, {'appeltaart': 'dat is lekker'})
    namenScherm.stop()

    # In objectsScreen.py
    puntenScherm = Screen('punten', {})
    puntenScherm.start()
    test2 = FormObject(None,{
        'w': '20px',
        'h': '20px'
    })
    puntenScherm.addData(puntenScherm.name, namenScherm.data)
    puntenScherm.stop()

    # In main.py
    print(namenScherm.getData(), puntenScherm.getData())

def draw():
    pass
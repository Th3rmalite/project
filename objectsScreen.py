from objects import *

# Definieer alle objecten in een scherm. Je kan deze dupliceren en aanpassen. 
# Hier kan je ook aanpassen wat er gebeurt als je ergens overheen gaat met je muis.

objectScreen = Screen({
    'background-color': rgb(255,255,255)
})

def settings():
    size(screen['w'], screen['h'])

def setup():
    test = FormObject(None,{
        'w': '50%',
        'h': '10%'
    })
    print(test.properties.getProperties())
    test['h'] = 50
    print(test['h'])
    test['h'] = '20%'
    print(test['h'])

def draw():
    pass
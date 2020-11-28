import invoerscherm
import puntenscherm

screenSize = [1080, 720]

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    #invoerscherm.setup()
    puntenscherm.setup([("Vincent","zwart"),("beide Dylans","wit"),("beide Dylans","rood"),("beide Dylans","blauw")])
        
def draw():
    #invoerscherm.draw()
    puntenscherm.draw()
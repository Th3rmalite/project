import invoerscherm
import puntenscherm

screenSize = [1080, 720]
count = 1

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    invoerscherm.setup()
    puntenscherm.setup(lijstmetnamen)
        
        
def draw():
    invoerscherm.draw()
    puntenscherm.draw()
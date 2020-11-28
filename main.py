import invoerscherm

screenSize = [1080, 720]

def settings():
    size(screenSize[0], screenSize[1])

def setup():
    invoerscherm.setup()
        
def draw():
    invoerscherm.draw()
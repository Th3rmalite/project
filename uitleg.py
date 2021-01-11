offset = 0
mul = 1.5
message = "move the pieces to the player that captured it"
piece = loadImage("pawn.png")
cursor = loadImage("mouse.png")
cursor.resize(100, 100)

screenSize = [1080, 720]

def settings():
    size(screenSize[0], screenSize[1])

def draw():  
    global offset, mul
    
    if offset > 200:
        mul = -1.5
    elif offset < 0:
        mul = 1.5
        
    background(90)
    image(piece, 450, 100 + offset)
    image(cursor, 500, 130 + offset)
    text(message, 450, 50)
    
    offset += mul
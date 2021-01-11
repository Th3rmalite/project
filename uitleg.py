offset = 0
mul = 1.5
message = "move the pieces to the player that captured it"
piece = loadImage("pawn.png")
cursor = loadImage("mouse.png")
cursor.resize(100, 100)

screenSize = [1080, 720]

def draw():  
    global offset, mul
    
    textAlign(CENTER)
    
    if offset > 200:
        mul = -1.5
    elif offset < 0:
        mul = 1.5
        
    background(90)
    image(piece, 450, 100 + offset)
    image(cursor, 500, 130 + offset)
    text(message, 540, 50)
    
    offset += mul
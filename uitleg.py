offset = 0
mul = 2
message = "Sleep het speelstuk naar jouw vak wanneer het is geslagen"
piece = loadImage("pawn.png")
cursor = loadImage("mouse.png")
cursor.resize(100, 100)

screenSize = [1080, 720]

def setup():
    textFont(loadFont('OpenSans-Bold-48.vlw'), 36)

def draw():
    textFont(loadFont('OpenSans-Bold-48.vlw'), 36)
    global offset, mul
    
    textAlign(CENTER)
    
    if offset > 150:
        mul = -2
    elif offset < 0:
        mul = 2
        
    background(90)
    image(piece, 450, 180 + offset)
    image(cursor, 500, 210 + offset)
    text(message, 540, 100)
    textFont(loadFont('OpenSans-Bold-48.vlw'), 12)
    text('(klik op "ga verder" om naar het volgende scherm te gaan)', 540, 120)
    
    offset += mul
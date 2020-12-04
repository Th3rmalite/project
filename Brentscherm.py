spelers = 4
colors = ['white','red']
def setup():
    size(1080,720)
    
def draw():
    global spelers
    bord = loadImage('download.png')
    
    paard_wit = loadImage('paard_wit.png')
    paard_rood = loadImage('paard_rood.png')
    paard_blauw = loadImage('paard_blauw.png')
    paard_zwart = loadImage('paard_zwart.png')
    
    toren_wit = loadImage('toren_wit.png')
    toren_rood = loadImage('toren_rood.png')
    toren_blauw = loadImage('toren_blauw.png')
    toren_zwart = loadImage('toren_zwart.png')
    
    koning_wit = loadImage('koning_wit.png')
    koning_rood = loadImage('koning_rood.png')
    koning_blauw = loadImage('koning_blauw.png')
    koning_zwart = loadImage('koning_zwart.png')
    
    koningin_wit = loadImage('koningin_wit.png')
    koningin_rood = loadImage('koningin_rood.png')
    koningin_blauw = loadImage('koningin_blauw.png')
    koningin_zwart = loadImage('koningin_zwart.png')
    
    pion_wit = loadImage('pion_wit.png')
    pion_rood = loadImage('pion_rood.png')
    pion_blauw = loadImage('pion_blauw.png')
    pion_zwart = loadImage('pion_zwart.png')
    
    background(255)
    fill(0)
    textSize(50)
    if spelers > 4:
        text('Het spel is speelbaar met 4 personen,',100,50)
        text('U bent over het limiet.',100,100)
    if spelers < 2:
        text('Het spel is speelbaar met 2 personen,',100,50)
        text('U bent onder het minimale aantal.',100,100)
    if spelers == 4:
        textSize(35)
        image(bord,50,50,100,100)
        text('x32, 8 per speler',150,145)
        if 'white' in colors:
            image(pion_wit,50,200,40,50)
            text('x6',100,245)
            image(koning_wit,45,250,50,60)
            text('x1',100,300)
            image(koningin_wit,45,310,50,50)
            text('x1',100,350)
            image(toren_wit,50,360,40,50)
            text('x2',100,400)
            image(paard_wit,50,410,40,50)
            text('x2',100,450)
        if 'red' in colors:
            image(pion_rood,195,200,40,50)
            text('x6',240,245)
            image(koning_rood,190,250,50,60)
            text('x1',240,300)
            image(koningin_rood,190,310,50,50)
            text('x1',240,350)
            image(toren_rood,195,360,40,50)
            text('x2',240,400)
            image(paard_rood,195,410,40,50)
            text('x2',240,450)
    if spelers == 3:
        textSize(35)
        image(bord,50,50,100,100)
        text('x27, 9 per speler',150,145)
        if 'white' in colors:
            image(pion_wit,50,200,40,50)
            text('x18, 6 per speler',100,245)
            image(koning_wit,45,250,50,60)
            text('x3, 1 per speler',100,300)
            image(koningin_wit,45,310,50,50)
            text('x3, 1 per speler',100,350)
            image(toren_wit,50,360,40,50)
            text('x6, 2 per speler',100,400)
            image(paard_wit,50,410,40,50)
            text('x6, 2 per speler',100,450)
    if spelers == 2:
        textSize(35)
        image(bord,50,50,100,100)
        text('x20, 10 per speler',150,145)
        if 'white' in colors:
            image(pion_wit,50,200,40,50)
            text('x12, 6 per speler',100,245)
            image(koning_wit,45,250,50,60)
            text('x2, 1 per speler',100,300)
            image(koningin_wit,45,310,50,50)
            text('x2, 1 per speler',100,350)
            image(toren_wit,50,360,40,50)
            text('x4, 2 per speler',100,400)
            image(paard_wit,50,410,40,50)
            text('x4, 2 per speler',100,450)
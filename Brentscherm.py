spelers = 4
colors = ['white','red','black','blue']
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
        image(bord,400,50,100,100)
        text('x32, 8 per speler',500,145)
        
        image(pion_wit,200,200,40,50)
        image(koning_wit,195,250,50,60)
        image(koningin_wit,195,310,50,50)
        image(toren_wit,200,360,40,50)
        image(paard_wit,200,410,40,50)

        image(pion_rood,345,200,40,50)
        image(koning_rood,340,250,50,60)
        image(koningin_rood,340,310,50,50)
        image(toren_rood,345,360,40,50)
        image(paard_rood,345,410,40,50)

        image(pion_blauw,490,200,40,50)
        image(koning_blauw,485,250,50,60)
        image(koningin_blauw,485,310,50,50)
        image(toren_blauw,490,360,40,50)
        image(paard_blauw,490,410,40,50)

        image(pion_zwart,635,200,40,50)
        image(koning_zwart,630,250,50,60)
        image(koningin_zwart,630,310,50,50)
        image(toren_zwart,635,360,40,50)
        image(paard_zwart,635,410,40,50)
        if 'white' in colors:
            text('x6',250,245) # pion_wit
            text('x1',250,300) # koning_wit
            text('x1',250,350) # koningin_wit
            text('x2',250,400) # toren_wit
            text('x2',250,450) # paard_wit
        if 'red' in colors:
            text('x6',390,245) # pion_rood
            text('x1',390,300) # koning_rood
            text('x1',390,350) # koningin_rood
            text('x2',390,400) # toren_rood
            text('x2',390,450) # paard_rood
        if 'blue' in colors:
            text('x6',540,245) # pion_blauw
            text('x1',540,300) # koning_blauw
            text('x1',540,350) # koningin_blauw
            text('x2',540,400) # toren_blauw
            text('x2',540,450) # paard_blauw
        if 'black' in colors:
            text('x6',685,245) # pion_zwart
            text('x1',685,300) # koning_zwart
            text('x1',685,350) # koningin_zwart
            text('x2',685,400) # toren_zwart
            text('x2',685,450) # paard_zwart
    if spelers == 3:
        textSize(35)
        image(bord,50,50,100,100)
        text('x27, 9 per speler',150,145)
        
        image(pion_wit,50,200,40,50)
        image(koning_wit,45,250,50,60)
        image(koningin_wit,45,310,50,50)
        image(toren_wit,50,360,40,50)
        image(paard_wit,50,410,40,50)

        image(pion_rood,195,200,40,50)
        image(koning_rood,190,250,50,60)
        image(koningin_rood,190,310,50,50)
        image(toren_rood,195,360,40,50)
        image(paard_rood,195,410,40,50)

        image(pion_blauw,340,200,40,50)
        image(koning_blauw,335,250,50,60)
        image(koningin_blauw,335,310,50,50)
        image(toren_blauw,340,360,40,50)
        image(paard_blauw,340,410,40,50)

        image(pion_zwart,485,200,40,50)
        image(koning_zwart,480,250,50,60)
        image(koningin_zwart,480,310,50,50)
        image(toren_zwart,485,360,40,50)
        image(paard_zwart,485,410,40,50)
        if 'white' in colors:
            text('x6',100,245) # pion_wit
            text('x1',100,300) # koning_wit
            text('x1',100,350) # koningin_wit
            text('x2',100,400) # toren_wit
            text('x2',100,450) # paard_wit
        if 'red' in colors:
            text('x6',240,245) # pion_rood
            text('x1',240,300) # koning_rood
            text('x1',240,350) # koningin_rood
            text('x2',240,400) # toren_rood
            text('x2',240,450) # paard_rood
        if 'blue' in colors:
            text('x6',390,245) # pion_blauw
            text('x1',390,300) # koning_blauw
            text('x1',390,350) # koningin_blauw
            text('x2',390,400) # toren_blauw
            text('x2',390,450) # paard_blauw
        if 'black' in colors:
            text('x6',535,245) # pion_zwart
            text('x1',535,300) # koning_zwart
            text('x1',535,350) # koningin_zwart
            text('x2',535,400) # toren_zwart
            text('x2',535,450) # paard_zwart
    if spelers == 2:
        textSize(35)
        image(bord,50,50,100,100)
        text('x20, 10 per speler',150,145)
        
        image(pion_wit,50,200,40,50)
        image(koning_wit,45,250,50,60)
        image(koningin_wit,45,310,50,50)
        image(toren_wit,50,360,40,50)
        image(paard_wit,50,410,40,50)

        image(pion_rood,195,200,40,50)
        image(koning_rood,190,250,50,60)
        image(koningin_rood,190,310,50,50)
        image(toren_rood,195,360,40,50)
        image(paard_rood,195,410,40,50)

        image(pion_blauw,340,200,40,50)
        image(koning_blauw,335,250,50,60)
        image(koningin_blauw,335,310,50,50)
        image(toren_blauw,340,360,40,50)
        image(paard_blauw,340,410,40,50)

        image(pion_zwart,485,200,40,50)
        image(koning_zwart,480,250,50,60)
        image(koningin_zwart,480,310,50,50)
        image(toren_zwart,485,360,40,50)
        image(paard_zwart,485,410,40,50)
        if 'white' in colors:
            text('x6',100,245) # pion_wit
            text('x1',100,300) # koning_wit
            text('x1',100,350) # koningin_wit
            text('x2',100,400) # toren_wit
            text('x2',100,450) # paard_wit
        if 'red' in colors:
            text('x6',240,245) # pion_rood
            text('x1',240,300) # koning_rood
            text('x1',240,350) # koningin_rood
            text('x2',240,400) # toren_rood
            text('x2',240,450) # paard_rood
        if 'blue' in colors:
            text('x6',390,245) # pion_blauw
            text('x1',390,300) # koning_blauw
            text('x1',390,350) # koningin_blauw
            text('x2',390,400) # toren_blauw
            text('x2',390,450) # paard_blauw
        if 'black' in colors:
            text('x6',535,245) # pion_zwart
            text('x1',535,300) # koning_zwart
            text('x1',535,350) # koningin_zwart
            text('x2',535,400) # toren_zwart
            text('x2',535,450) # paard_zwart
spelers = 4
colors = ['red','black','white','blue']
x = 75
def setup():
    size(1080,720)
    frameRate(5)
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
        textSize(25)
        text('This game is meant to be played with 4 or less players,',100,300)
        text('You are currently over the required amount of players to play.',100,325)
        text("I don't even know how you got this message, since it isn't possible, but good job.",100,350)
    if spelers < 2:
        textSize(25)
        text('This game is meant to be played with 2 or more players,',100,300)
        text('You are currently under the required amount of players to play.',100,325)
    if spelers == 4:
        fill(50, 50, 50)
        rect(125, 40, 850, 450)
        fill(255)
        textSize(20)
        image(bord,490,50,100,100)
        text('Total of 32 pieces, Divide them between all players and place them to your likings.',150,175)
        textSize(30)
        
        red_used = False
        blue_used = False
        black_used = False
        if 'white' in colors:
            text('x6',250+x,245) # pion_wit
            text('x1',250+x,300) # koning_wit
            text('x1',250+x,350) # koningin_wit
            text('x2',250+x,400) # toren_wit
            text('x2',250+x,450) # paard_wit
            image(pion_wit,200+x,200,40,50)
            image(koning_wit,195+x,250,50,60)
            image(koningin_wit,195+x,310,50,50)
            image(toren_wit,200+x,360,40,50)
            image(paard_wit,200+x,410,40,50)
        else:
            if 'red' in colors and red_used == False:
                red_used = True
                text('x6',250+x,245) # pion_rood
                text('x1',250+x,300) # koning_rood
                text('x1',250+x,350) # koningin_rood
                text('x2',250+x,400) # toren_rood
                text('x2',250+x,450) # paard_rood
                image(pion_rood,200+x,200,40,50)
                image(koning_rood,195+x,250,50,60)
                image(koningin_rood,195+x,310,50,50)
                image(toren_rood,200+x,360,40,50)
                image(paard_rood,200+x,410,40,50)
            elif 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',250+x,245) # pion_blauw
                text('x1',250+x,300) # koning_blauw
                text('x1',250+x,350) # koningin_blauw
                text('x2',250+x,400) # toren_blauw
                text('x2',250+x,450) # paard_blauw
                image(pion_blauw,200+x,200,40,50)
                image(koning_blauw,195+x,250,50,60)
                image(koningin_blauw,195+x,310,50,50)
                image(toren_blauw,200+x,360,40,50)
                image(paard_blauw,200+x,410,40,50)

        if 'red' in colors and red_used == False:
            red_used = True
            text('x6',390+x,245) # pion_rood
            text('x1',390+x,300) # koning_rood
            text('x1',390+x,350) # koningin_rood
            text('x2',390+x,400) # toren_rood
            text('x2',390+x,450) # paard_rood
            image(pion_rood,345+x,200,40,50)
            image(koning_rood,340+x,250,50,60)
            image(koningin_rood,340+x,310,50,50)
            image(toren_rood,345+x,360,40,50)
            image(paard_rood,345+x,410,40,50)
        else:
            if 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',390+x,245) # pion_blauw
                text('x1',390+x,300) # koning_blauw
                text('x1',390+x,350) # koningin_blauw
                text('x2',390+x,400) # toren_blauw
                text('x2',390+x,450) # paard_blauw
                image(pion_blauw,345+x,200,40,50)
                image(koning_blauw,340+x,250,50,60)
                image(koningin_blauw,340+x,310,50,50)
                image(toren_blauw,345+x,360,40,50)
                image(paard_blauw,345+x,410,40,50)
            elif 'black' in colors and black_used == False:
                black_used = True
                text('x6',390+x,245) # pion_zwart
                text('x1',390+x,300) # koning_zwart
                text('x1',390+x,350) # koningin_zwart
                text('x2',390+x,400) # toren_zwart
                text('x2',390+x,450) # paard_zwart
                image(pion_zwart,345+x,200,40,50)
                image(koning_zwart,340+x,250,50,60)
                image(koningin_zwart,340+x,310,50,50)
                image(toren_zwart,345+x,360,40,50)
                image(paard_zwart,345+x,410,40,50)

        if 'blue' in colors and blue_used == False:
            blue_used = True
            text('x6',540+x,245) # pion_blauw
            text('x1',540+x,300) # koning_blauw
            text('x1',540+x,350) # koningin_blauw
            text('x2',540+x,400) # toren_blauw
            text('x2',540+x,450) # paard_blauw
            image(pion_blauw,490+x,200,40,50)
            image(koning_blauw,485+x,250,50,60)
            image(koningin_blauw,485+x,310,50,50)
            image(toren_blauw,490+x,360,40,50)
            image(paard_blauw,490+x,410,40,50)
        else:
            if 'black' in colors and black_used == False:
                black_used = True
                text('x6',540+x,245) # pion_blauw
                text('x1',540+x,300) # koning_blauw
                text('x1',540+x,350) # koningin_blauw
                text('x2',540+x,400) # toren_blauw
                text('x2',540+x,450) # paard_blauw
                image(pion_zwart,490+x,200,40,50)
                image(koning_zwart,485+x,250,50,60)
                image(koningin_zwart,485+x,310,50,50)
                image(toren_zwart,490+x,360,40,50)
                image(paard_zwart,490+x,410,40,50)
        if 'black' in colors and black_used == False:
            black_used = True
            text('x6',685+x,245) # pion_zwart
            text('x1',685+x,300) # koning_zwart
            text('x1',685+x,350) # koningin_zwart
            text('x2',685+x,400) # toren_zwart
            text('x2',685+x,450) # paard_zwart
            image(pion_zwart,635+x,200,40,50)
            image(koning_zwart,630+x,250,50,60)
            image(koningin_zwart,630+x,310,50,50)
            image(toren_zwart,635+x,360,40,50)
            image(paard_zwart,635+x,410,40,50)
    if spelers == 3:
        fill(127)
        rect(125, 40, 850, 150)
        fill(0)
        textSize(20)
        image(bord,490,50,100,100)
        text('Total of 27 pieces, Divide them between all players and place them to your likings.',150,175)
        textSize(30)
        red_used = False
        blue_used = False
        black_used = False
        if 'white' in colors:
            text('x6',250+x,245) # pion_wit
            text('x1',250+x,300) # koning_wit
            text('x1',250+x,350) # koningin_wit
            text('x2',250+x,400) # toren_wit
            text('x2',250+x,450) # paard_wit
            image(pion_wit,200+x,200,40,50)
            image(koning_wit,195+x,250,50,60)
            image(koningin_wit,195+x,310,50,50)
            image(toren_wit,200+x,360,40,50)
            image(paard_wit,200+x,410,40,50)
        else:
            if 'red' in colors and red_used == False:
                red_used = True
                text('x6',250+x,245) # pion_rood
                text('x1',250+x,300) # koning_rood
                text('x1',250+x,350) # koningin_rood
                text('x2',250+x,400) # toren_rood
                text('x2',250+x,450) # paard_rood
                image(pion_rood,200+x,200,40,50)
                image(koning_rood,195+x,250,50,60)
                image(koningin_rood,195+x,310,50,50)
                image(toren_rood,200+x,360,40,50)
                image(paard_rood,200+x,410,40,50)
            elif 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',250+x,245) # pion_blauw
                text('x1',250+x,300) # koning_blauw
                text('x1',250+x,350) # koningin_blauw
                text('x2',250+x,400) # toren_blauw
                text('x2',250+x,450) # paard_blauw
                image(pion_blauw,200+x,200,40,50)
                image(koning_blauw,195+x,250,50,60)
                image(koningin_blauw,195+x,310,50,50)
                image(toren_blauw,200+x,360,40,50)
                image(paard_blauw,200+x,410,40,50)

        if 'red' in colors and red_used == False:
            red_used = True
            text('x6',390+x,245) # pion_rood
            text('x1',390+x,300) # koning_rood
            text('x1',390+x,350) # koningin_rood
            text('x2',390+x,400) # toren_rood
            text('x2',390+x,450) # paard_rood
            image(pion_rood,345+x,200,40,50)
            image(koning_rood,340+x,250,50,60)
            image(koningin_rood,340+x,310,50,50)
            image(toren_rood,345+x,360,40,50)
            image(paard_rood,345+x,410,40,50)
        else:
            if 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',390+x,245) # pion_blauw
                text('x1',390+x,300) # koning_blauw
                text('x1',390+x,350) # koningin_blauw
                text('x2',390+x,400) # toren_blauw
                text('x2',390+x,450) # paard_blauw
                image(pion_blauw,345+x,200,40,50)
                image(koning_blauw,340+x,250,50,60)
                image(koningin_blauw,340+x,310,50,50)
                image(toren_blauw,345+x,360,40,50)
                image(paard_blauw,345+x,410,40,50)
            elif 'black' in colors and black_used == False:
                black_used = True
                text('x6',390+x,245) # pion_zwart
                text('x1',390+x,300) # koning_zwart
                text('x1',390+x,350) # koningin_zwart
                text('x2',390+x,400) # toren_zwart
                text('x2',390+x,450) # paard_zwart
                image(pion_zwart,345+x,200,40,50)
                image(koning_zwart,340+x,250,50,60)
                image(koningin_zwart,340+x,310,50,50)
                image(toren_zwart,345+x,360,40,50)
                image(paard_zwart,345+x,410,40,50)

        if 'blue' in colors and blue_used == False:
            blue_used = True
            text('x6',540+x,245) # pion_blauw
            text('x1',540+x,300) # koning_blauw
            text('x1',540+x,350) # koningin_blauw
            text('x2',540+x,400) # toren_blauw
            text('x2',540+x,450) # paard_blauw
            image(pion_blauw,490+x,200,40,50)
            image(koning_blauw,485+x,250,50,60)
            image(koningin_blauw,485+x,310,50,50)
            image(toren_blauw,490+x,360,40,50)
            image(paard_blauw,490+x,410,40,50)
        else:
            if 'black' in colors and black_used == False:
                black_used = True
                text('x6',540+x,245) # pion_blauw
                text('x1',540+x,300) # koning_blauw
                text('x1',540+x,350) # koningin_blauw
                text('x2',540+x,400) # toren_blauw
                text('x2',540+x,450) # paard_blauw
                image(pion_zwart,490+x,200,40,50)
                image(koning_zwart,485+x,250,50,60)
                image(koningin_zwart,485+x,310,50,50)
                image(toren_zwart,490+x,360,40,50)
                image(paard_zwart,490+x,410,40,50)
        if 'black' in colors and black_used == False:
            black_used = True
            text('x6',685+x,245) # pion_zwart
            text('x1',685+x,300) # koning_zwart
            text('x1',685+x,350) # koningin_zwart
            text('x2',685+x,400) # toren_zwart
            text('x2',685+x,450) # paard_zwart
            image(pion_zwart,635+x,200,40,50)
            image(koning_zwart,630+x,250,50,60)
            image(koningin_zwart,630+x,310,50,50)
            image(toren_zwart,635+x,360,40,50)
            image(paard_zwart,635+x,410,40,50)
    if spelers == 2:
        fill(127)
        rect(125, 40, 850, 150)
        fill(0)
        textSize(20)
        image(bord,490,50,100,100)
        text('Total of 20 pieces, Divide them between all players and place them to your likings.',150,175)
        textSize(30)
        red_used = False
        blue_used = False
        black_used = False
        if 'white' in colors:
            text('x6',250+x,245) # pion_wit
            text('x1',250+x,300) # koning_wit
            text('x1',250+x,350) # koningin_wit
            text('x2',250+x,400) # toren_wit
            text('x2',250+x,450) # paard_wit
            image(pion_wit,200+x,200,40,50)
            image(koning_wit,195+x,250,50,60)
            image(koningin_wit,195+x,310,50,50)
            image(toren_wit,200+x,360,40,50)
            image(paard_wit,200+x,410,40,50)
        else:
            if 'red' in colors and red_used == False:
                red_used = True
                text('x6',250+x,245) # pion_rood
                text('x1',250+x,300) # koning_rood
                text('x1',250+x,350) # koningin_rood
                text('x2',250+x,400) # toren_rood
                text('x2',250+x,450) # paard_rood
                image(pion_rood,200+x,200,40,50)
                image(koning_rood,195+x,250,50,60)
                image(koningin_rood,195+x,310,50,50)
                image(toren_rood,200+x,360,40,50)
                image(paard_rood,200+x,410,40,50)
            elif 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',250+x,245) # pion_blauw
                text('x1',250+x,300) # koning_blauw
                text('x1',250+x,350) # koningin_blauw
                text('x2',250+x,400) # toren_blauw
                text('x2',250+x,450) # paard_blauw
                image(pion_blauw,200+x,200,40,50)
                image(koning_blauw,195+x,250,50,60)
                image(koningin_blauw,195+x,310,50,50)
                image(toren_blauw,200+x,360,40,50)
                image(paard_blauw,200+x,410,40,50)

        if 'red' in colors and red_used == False:
            red_used = True
            text('x6',390+x,245) # pion_rood
            text('x1',390+x,300) # koning_rood
            text('x1',390+x,350) # koningin_rood
            text('x2',390+x,400) # toren_rood
            text('x2',390+x,450) # paard_rood
            image(pion_rood,345+x,200,40,50)
            image(koning_rood,340+x,250,50,60)
            image(koningin_rood,340+x,310,50,50)
            image(toren_rood,345+x,360,40,50)
            image(paard_rood,345+x,410,40,50)
        else:
            if 'blue' in colors and blue_used == False:
                blue_used = True
                text('x6',390+x,245) # pion_blauw
                text('x1',390+x,300) # koning_blauw
                text('x1',390+x,350) # koningin_blauw
                text('x2',390+x,400) # toren_blauw
                text('x2',390+x,450) # paard_blauw
                image(pion_blauw,345+x,200,40,50)
                image(koning_blauw,340+x,250,50,60)
                image(koningin_blauw,340+x,310,50,50)
                image(toren_blauw,345+x,360,40,50)
                image(paard_blauw,345+x,410,40,50)
            elif 'black' in colors and black_used == False:
                black_used = True
                text('x6',390+x,245) # pion_zwart
                text('x1',390+x,300) # koning_zwart
                text('x1',390+x,350) # koningin_zwart
                text('x2',390+x,400) # toren_zwart
                text('x2',390+x,450) # paard_zwart
                image(pion_zwart,345+x,200,40,50)
                image(koning_zwart,340+x,250,50,60)
                image(koningin_zwart,340+x,310,50,50)
                image(toren_zwart,345+x,360,40,50)
                image(paard_zwart,345+x,410,40,50)

        if 'blue' in colors and blue_used == False:
            blue_used = True
            text('x6',540+x,245) # pion_blauw
            text('x1',540+x,300) # koning_blauw
            text('x1',540+x,350) # koningin_blauw
            text('x2',540+x,400) # toren_blauw
            text('x2',540+x,450) # paard_blauw
            image(pion_blauw,490+x,200,40,50)
            image(koning_blauw,485+x,250,50,60)
            image(koningin_blauw,485+x,310,50,50)
            image(toren_blauw,490+x,360,40,50)
            image(paard_blauw,490+x,410,40,50)
        else:
            if 'black' in colors and black_used == False:
                black_used = True
                text('x6',540+x,245) # pion_blauw
                text('x1',540+x,300) # koning_blauw
                text('x1',540+x,350) # koningin_blauw
                text('x2',540+x,400) # toren_blauw
                text('x2',540+x,450) # paard_blauw
                image(pion_zwart,490+x,200,40,50)
                image(koning_zwart,485+x,250,50,60)
                image(koningin_zwart,485+x,310,50,50)
                image(toren_zwart,490+x,360,40,50)
                image(paard_zwart,490+x,410,40,50)
        if 'black' in colors and black_used == False:
            black_used = True
            text('x6',685+x,245) # pion_zwart
            text('x1',685+x,300) # koning_zwart
            text('x1',685+x,350) # koningin_zwart
            text('x2',685+x,400) # toren_zwart
            text('x2',685+x,450) # paard_zwart
            image(pion_zwart,635+x,200,40,50)
            image(koning_zwart,630+x,250,50,60)
            image(koningin_zwart,630+x,310,50,50)
            image(toren_zwart,635+x,360,40,50)
            image(paard_zwart,635+x,410,40,50)
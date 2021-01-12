from objects import *

def setup():
    global imageAll, count, texti, mouse, rect1, rect2, goBack
    size(1080, 720)
    background(190)
    manual = Screen(None, {})
    manual.start()
    goBack = Button(None, {
        'x': 95,
        'y': 690,
        'w': 160,
        'h': 40,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '201 138 38 255',
        'placeholder': 'Teruggaan',
        'radius': 5,
        'textSize': 18,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'textColor': '255 255 255 255',
        'font': 'OpenSans-Bold-48.vlw'
    })
    goBack.hover.setItems({
        'fill': '201 138 38 200',
        'w': 175,
        'h': 45,
        'textSize': 19
    })
    manual.stop()

    noStroke()
    fontList = PFont.list()
    noTint()
    textAlign(LEFT, CENTER)
    rectMode(CORNER)
    image0 = loadImage('whitepage.png')
    image1 = loadImage('handleidingpag1.png')
    image2 = loadImage('handleidingpag2.png')
    image3 = loadImage('handleidingpag3.png')
    image4 = loadImage('handleidingpag4.png')
    image5 = loadImage('handleidingpag5.png')
    image6 = loadImage('handleidingpag6.png')
    image7 = loadImage('handleidingpag7.png')
    image8 = loadImage('handleidingpag8.png')
    image9 = loadImage('handleidingpag9.png')
    image10 = loadImage('handleidingpag10.png')
    image11 = loadImage('handleidingpag11.png')
    image12 = loadImage('handleidingpag12.png')
    
    cover = image0.resize(449, 640)
    cover = image1.resize(449, 640)
    cover = image2.resize(449, 640)
    cover = image3.resize(449, 640)
    cover = image4.resize(449, 640)
    cover = image5.resize(449, 640)
    cover = image6.resize(449, 640)
    cover = image7.resize(449, 640)
    cover = image8.resize(449, 640)
    cover = image9.resize(449, 640)
    cover = image10.resize(449, 640)
    cover = image11.resize(449, 640)
    cover = image12.resize(449, 640)
    
    text1 = [600, 150, 135, 25]
    text2 = [600, 200, 160, 25]
    text3 = [600, 250, 100, 25]
    text4 = [600, 300, 290, 25]
    text5 = [600, 350, 105, 25]
    text6 = [600, 400, 190, 25]
    text7 = [600, 450, 135, 25]
    text8 = [600, 500, 150, 25]
    text9 = [600, 550, 115, 25]
    
    imageAll = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image0]
   
    texti = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    
    count = 0
    
    rect1 = [1040,295,30,30]
    rect2 = [10, 295, 30, 30]

    # inhoudsopgave
def inhoudsopgave():
    font1 = createFont("Georgia", 40)
    textFont(font1)
    fill(155,50,50)
    rect(595, 65, 150, 65)
    fill(255,255,255)
    text('Inhoud', 600, 100)
    textFont(pagefont)     
    fill(0)
    text('pagina 1', 480, 670)
    fill(0)
    text('pagina 2', 960, 670)

    

def draw():
    global pagefont, imageAll, count, a, b, texti, mouse
    goBack.draw()
    textAlign(LEFT, CENTER)
    rectMode(CORNER)
    pagefont = createFont("Droid Serif", 12)
    
    mouse = [mouseX, mouseY]
    
    # pagina schermen
    if count == 0:
        image(imageAll[10], 75, 15)
        image(imageAll[-1], 555,15)
        inhoudsopgave()
        if hover(mouse, rect2):
            cursor(HAND)
        else:
            cursor(ARROW) 


    if count == 1:
        image(imageAll[0], 75, 15)
        image(imageAll[1], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 3', 480, 670)
        fill(0)
        text('pagina 4', 960, 670)
        textFont(pagefont)
        if hover(mouse, rect2) or hover(mouse, rect1):
            cursor(HAND)
        else:
            cursor(ARROW)   
    if count == 2:
        image(imageAll[2], 75, 15)
        image(imageAll[3], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 5', 480, 670)
        fill(0)
        text('pagina 6', 960, 670)
        if hover(mouse, rect2) or hover(mouse, rect1):
            cursor(HAND)
        else:
            cursor(ARROW) 
    if count == 3:
        image(imageAll[4], 75, 15)
        image(imageAll[5], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 7', 480, 670)
        fill(0)
        text('pagina 8', 960, 670)
        if hover(mouse, rect2) or hover(mouse, rect1):
            cursor(HAND)
        else:
            cursor(ARROW) 
    if count == 4:
        image(imageAll[6], 75, 15)
        image(imageAll[7], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 9', 480, 670)
        fill(0)
        text('pagina 10', 960, 670)
        if hover(mouse, rect2) or hover(mouse, rect1):
            cursor(HAND)
        else:
            cursor(ARROW) 
    if count == 5:
        image(imageAll[8], 75, 15)
        image(imageAll[9], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 11', 480, 670)
        text('pagina 12', 960, 670)
        if hover(mouse, rect2) or hover(mouse, rect1):
            cursor(HAND)
        else:
            cursor(ARROW) 
    if count == 6:
        image(imageAll[10], 75, 15)
        image(imageAll[11], 555, 15)
        textFont(pagefont)
        fill(0)
        text('pagina 13', 480, 670)
        text('pagina 14', 960, 670)
        if hover(mouse, rect2):
            cursor(HAND)
        else:
            cursor(ARROW) 
    
    # 270, 705
    # 790, 705

    if count != 6:
        fill(255)
        triangle(1040,295,1040,325,1070,310)
    else:
        fill(190)
        triangle(1040,295,1040,325,1070,310)
    
    if count != 0:
        fill(255)
        triangle(40,295,40,325,10,310)
    else:
        fill(190)
        triangle(40,295,40,325,10,310)
    
        # hover functie op inhoudsopgave
    if count == 0:
        if hover(mouse, rect1) or hover(mouse, texti[0]) or hover(mouse, texti[1]) or hover(mouse, texti[2]) or hover(mouse, texti[3]) or hover(mouse, texti[4]) or hover(mouse, texti[5]) or hover(mouse, texti[6]) or hover(mouse, texti[7]) or hover(mouse, texti[8]):
            cursor(HAND)
            font2 = createFont("Serif Fonts", 20)
            textFont(font2)
            fill(0)
            if hover(mouse, texti[0]):
                fill(150,50,50)
                text('- Hoe begin je?', 600, 150)
            else:
                fill(0)
                text('- Hoe begin je?', 600, 150)    
            if hover(mouse, texti[1]):
                fill(150,50,50)
                text('- De speelstukken', 600, 200)
            else:
                fill(0)
                text('- De speelstukken', 600, 200)
            if hover(mouse, texti[2]):
                fill(150,50,50)
                text('- Aanvallen', 600, 250)
            else:
                fill(0)
                text('- Aanvallen', 600, 250)  
            if hover(mouse, texti[3]):
                fill(150,50,50)
                text('- Jouw speel richting/ verdedigen', 600, 300)
            else:
                fill(0)
                text('- Jouw speel richting/ verdedigen', 600, 300)
            if hover(mouse, texti[4]):
                fill(150,50,50)
                text('- Blokkades', 600, 350)
            else:
                fill(0)
                text('- Blokkades', 600, 350)
            if hover(mouse, texti[5]):
                fill(150,50,50)
                text('- Het dynamisch bord', 600, 400)
            else:
                fill(0)
                text('- Het dynamisch bord', 600, 400)
            if hover(mouse, texti[6]):
                fill(150,50,50)
                text('- Wat is matten', 600, 450)
            else:
                fill(0)
                text('- Wat is matten', 600, 450)
            if hover(mouse, texti[7]):
                fill(150,50,50)
                text('- Bordsjablonnen', 600, 500)
            else:
                fill(0)
                text('- Bordsjablonnen', 600, 500)
            if hover(mouse, texti[8]):
                fill(150,50,50)
                text('- Onderdelen', 600, 550)
            else:
                fill(0)
                text('- Onderdelen', 600, 550)
        else:
            cursor(ARROW)
            font2 = createFont("Serif Fonts", 20)
            textFont(font2)
            fill(0)
            text('- Hoe begin je?', 600, 150)
            text('- De speelstukken', 600, 200)
            text('- Aanvallen', 600, 250)
            text('- Jouw speel richting/ verdedigen', 600, 300)
            text('- Blokkades', 600, 350)
            text('- Het dynamisch bord', 600, 400)
            text('- Wat is matten', 600, 450)
            text('- Bordsjablonnen', 600, 500)
            text('- Onderdelen', 600, 550)
    global mouseUp   
    if not mousePressed:
        mouseUp = True
    if mousePressed and mouseUp:
        mouseUp = False
        global count, texti, mouse
    


        #navigatie
        if hover(mouse, rect1):
            if count != 6:
                count = count + 1
        if hover(mouse, rect2):
            if count != 0:
                count = count - 1
        
        if count != 100:
            if hover(mouse, texti[0]) or hover(mouse, texti[1]):
                count = 1
            elif hover(mouse, texti[2]):
                count = 2
            elif hover(mouse, texti[3]) or hover(mouse, texti[4]):
                count = 3
            elif hover(mouse, texti[5]):
                count = 4
            elif hover(mouse, texti[6]) or hover(mouse, texti[7]):
                count = 5
            elif hover(mouse, texti[8]):
                count = 6



    # hover functie defined
def hover(a,b):
    isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
    isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
    if (isBetweenY and isBetweenX):
        return True
    return False
    
    # muis klik functie

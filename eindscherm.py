def setup(scores):
    global score
    score = scores
    size(1080,720)
    frameRate(5)
    global winner
    winner = score[0].player_color
    

def draw():
    global score
    koning_wit = loadImage('koning_wit.png')
    koning_rood = loadImage('koning_rood.png')
    koning_blauw = loadImage('koning_blauw.png')
    koning_zwart = loadImage('koning_zwart.png')
    naam = score[0].name
    background(255)
    fill(0)
    textSize(45)
    fill(238,232,170)
    rectMode(CENTER)
    rect(540, 210, 650, 280, 20)
    stroke(50, 50, 50)
    strokeWeight(2)
    imageMode(CENTER)
    textAlign(CENTER)
    if winner == 'blue':
        fill(0,0,255)
        text(naam,540,150)
        fill(30)
        textSize(35)
        text('is the winner! Congratulations!',540,200)
        image(koning_blauw,540,270,100,120)
    if winner == 'black':
        fill(0,0,0)
        text(naam,540,150)
        fill(30)
        textSize(35)
        text('is the winner! Congratulations!',540,200)
        image(koning_zwart,540,270,100,120)
    if winner == 'white':
        fill(50,50,50)
        rectMode(CENTER)
        rect(540, 210, 650, 280, 20)
        fill(255,255,255)
        text(naam,540,150)
        fill(150)
        textSize(35)
        text('is the winner! Congratulations!',540,200)
        image(koning_wit,540,270,100,120)
    if winner == 'red':
        fill(255,0,0)
        text(naam,540,150)
        fill(30)
        textSize(35)
        text('is the winner! Congratulations!',540,200)
        image(koning_rood,540,270,100,120)
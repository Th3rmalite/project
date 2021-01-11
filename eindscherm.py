winner = 'blue'
def setup():
    size(1080,720)
    frameRate(5)
def draw():
    koning_wit = loadImage('koning_wit.png')
    koning_rood = loadImage('koning_rood.png')
    koning_blauw = loadImage('koning_blauw.png')
    koning_zwart = loadImage('koning_zwart.png')
    background(255)
    fill(0)
    textSize(45)
    fill(50, 50, 50)
    rect(125, 40, 850, 450)
    fill(255)
    if winner == 'blue':
        fill(0,0,255)
        text('Blue',160,150)
        fill(0)
        text('is the winner! Congratulations!',260,150)
        image(koning_blauw,425,200,200,240)
    if winner == 'black':
        fill(0,0,0)
        text('Black',150,150)
        fill(255)
        text('is the winner! Congratulations!',270,150)
        image(koning_zwart,425,200,200,240)
    if winner == 'white':
        fill(255,255,255)
        text('White',140,150)
        fill(0)
        text('is the winner! Congratulations!',270,150)
        image(koning_wit,425,200,200,240)
    if winner == 'red':
        fill(255,0,0)
        text('red',170,150)
        fill(0)
        text('is the winner! Congratulations!',250,150)
        image(koning_rood,425,200,200,240)
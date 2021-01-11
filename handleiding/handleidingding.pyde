

def setup():
    global imageAll, count
    size(1080, 720)
    background(190)
    noStroke()
    
    
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
    
    
    cover = image1.resize(470, 670)
    cover = image2.resize(470, 670)
    cover = image3.resize(470, 670)
    cover = image4.resize(470, 670)
    cover = image5.resize(470, 670)
    cover = image6.resize(470, 670)
    cover = image7.resize(470, 670)
    cover = image8.resize(470, 670)
    cover = image9.resize(470, 670)
    cover = image10.resize(470, 670)
    cover = image11.resize(470, 670)
    cover = image12.resize(470, 670)
    
    imageAll = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12]
    
    count = 0
    

def draw():
    global image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, imageAll, count, a, b
    
    if count == 0:
        image(imageAll[0], 55, 15)
        image(imageAll[1], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 1', 250, 705)
        fill(0)
        text('page 2', 790, 705)
    if count == 1:
        image(imageAll[2], 55, 15)
        image(imageAll[3], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 3', 250, 705)
        fill(0)
        text('page 4', 790, 705)
    if count == 2:
        image(imageAll[4], 55, 15)
        image(imageAll[5], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 5', 250, 705)
        fill(0)
        text('page 6', 790, 705)
    if count == 3:
        image(imageAll[6], 55, 15)
        image(imageAll[7], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 7', 250, 705)
        fill(0)
        text('page 8', 790, 705)
    if count == 4:
        image(imageAll[8], 55, 15)
        image(imageAll[9], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 9', 250, 705)
        fill(0)
        text('page 10', 790, 705)
    if count == 5:
        image(imageAll[10], 55, 15)
        image(imageAll[11], 555, 15)
        fill(255)
        rect(245,690,50,20)
        fill(255)
        rect(785,690,50,20)
        fill(0)
        text('page 11', 250, 705)
        fill(0)
        text('page 12', 790, 705)
    

    if count != 5:
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

    a = [mouseX, mouseY]
    b = [1040, 295, 30, 30]
    

def hover(a,b):
    isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
    isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
    if (isBetweenY and isBetweenX):
        return True
    return False
    
def mousePressed():
    global count
    rect = [1040,295,30,30]
    mouse = [mouseX,mouseY]
    if hover(mouse,rect):
        if count != 5:
            count = count + 1
    if 10 < mouseX < 40 and 295 < mouseY < 325:
        if count != 0:
            count = count - 1
        

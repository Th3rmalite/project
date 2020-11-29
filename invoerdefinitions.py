import functions as f
import invoerscherm
import main

palette = {
    'white'         :   color(238, 239, 240),
    'black'         :   color(50, 50, 50),
    'gray'          :   color(213, 216, 219),
    'gray_hover'    :   color(203, 206, 209),
    'dark_gray'     :   color(193, 196, 199),
    'light_blue'    :   color(204, 216, 223),
    'blue'          :   color(77, 107, 164),
    'red'           :   color(229, 56, 59),
    'transparent'   :   color(220, 220, 220, 100),
    'solid_white'   :   color(255, 255, 255),
    'green'         :   color(138, 201, 38),
    'player_colors' :   [
                        color(248, 249, 250),   # white
                        color(20, 23, 26),      # black
                        color(164, 22, 26),     # red
                        color(3, 4, 94)         # blue
                        ]
}

players = [] # table
cards = [] # table
textInputs = [] # table
colorPickers = [] # table
navigationButtons = [] # table

screenSize = [1080, 720]
index = 0

def setupCards():
    global screenSize
    global Card
    global TextInput
    global ColorPicker
    textSize(16)
    for i in range(4):
        cards.append(Card(i, screenSize[0]/2, 130, 420, 140, 10, 'solid_white'))
        colorPickers.append(ColorPicker(i, cards[i].x, cards[i].y, 35, 42))
        textInputs.append(TextInput(i, cards[i].x, cards[i].y, 200))
        cards[i].shadow(2, 2)
        players.append(['Name', 'blue', cards[i], colorPickers[i]])

def setupRest():
    navigationButtons.append(NavigationButton('Puntenscherm', 0, 0, 130, 50, 'BOTTOM_RIGHT'))
    navigationButtons[0].shadow(1, 1)
    background(color(palette['gray']))

def drawCards(index):
    global cards
    cards[index].draw()
    textInputs[index].draw()
    colorPickers[index].draw()

def drawRest():
    navigationButtons[0].draw()

class NavigationButton:

    def __init__(self, referral, x, y, w, h, anchor = 'NONE'):
        self.ref = referral
        self.anchor = anchor
        location = f.locationAnchor(anchor)
        self.x = location[0] + x
        self.y = location[1] + y
        self.w = w
        self.h = h
        self.bevel = 20
        self.shadowRadius = 3
        self.selected = False
    
    def draw(self):
        fill(palette['green'])
        noStroke()
        self.changeState()
        rect(self.x, self.y, self.w, self.h, self.bevel)

    def hover(self):
        if f.hover([mouseX,mouseY],[self.x - self.w / 2, self.y - self.h / 2, self.x, self.y]):
            return True
    
    def changeState(self):
        if self.hover() and not self.selected:
            fill(palette['green'] + color(10,10,10))
        if self.selected or (self.hover() and mouseButton == LEFT):
            self.selected = True
            fill(palette['green'] - color(30,30,30))


    def shadow(self, offsetX, offsetY, samples = 64):
        rectMode(CENTER)
        noStroke()
        fill(0,0,0,1)
        for i in range(samples):
            rect(self.x + offsetX, self.y + offsetY, self.w + self.shadowRadius - i * .1, self.h + self.shadowRadius - i * .1, self.bevel)


class Card:

    def __init__(self, index, x, y, w, h, spacing, cardColor):
        global players
        self.index = index
        self.cardColor = cardColor
        self.x = x
        self.y = y + (index * (h + spacing))
        self.w = w
        self.h = h    
        self.spacing = spacing
        self.bevel = 7
        self.shadowRadius = 6
        
    
    def draw(self):
        fill(palette[self.cardColor])
        # self.hover() # Make it so that self.hover() doesn't affect fill when not hovered.
        noStroke()
        rect(self.x, self.y, self.w, self.h, self.bevel)
    
    def shadow(self, offsetX, offsetY, samples = 64):
        rectMode(CENTER)
        noStroke()
        fill(0,0,0,1)
        for i in range(samples):
            rect(self.x + offsetX, self.y + offsetY, self.w + self.shadowRadius - i * .1, self.h + self.shadowRadius - i * .1, self.bevel)


class ColorPicker:

    def __init__(self, index, x, y, extent, spacing):
        self.index = index
        self.x = x + (80 - extent)
        self.y = y
        self.extent = extent
        self.spacing = spacing
        self.colorNodes = []
        self.previousSelected = ''
        rectMode(CENTER)
        for i in range(len(palette['player_colors'])):
            self.colorNodes.append([False, palette['player_colors'][i]])
    
    def draw(self):
        for i in range(len(palette['player_colors'])):
            stroke(0,0,0)
            fill(self.colorNodes[i][1])
            self.changeState(i)
            circle(self.x + i * self.spacing, self.y, self.extent)
    
    def hover(self, index):
        if f.hover([mouseX,mouseY],[self.x + index * self.spacing - self.extent / 2, self.y - self.extent / 2, self.extent, self.extent]):
            return True

    def changeState(self, index):
        if self.colorNodes[index][0] or (self.hover(index) and mouseButton == LEFT):
            if type(self.previousSelected) == int:
                self.colorNodes[self.previousSelected][0] = False
            self.previousSelected = index
            self.colorNodes[index][0] = True
            players[self.index][2].cardColor = self.getColor(palette['player_colors'][index])
            fill(palette['player_colors'][index] - color(0, 0, 0, 150))
            stroke(0,155,0)
            strokeWeight(2)
            for i in range(4):
                if players[i][3].colorNodes[index][0] and players[i] != players[self.index]:
                    players[i][3].colorNodes[index][0] = False
                    players[i][2].cardColor = 'solid_white'
            players[self.index][1] = self.getColor(palette['player_colors'][index])
        elif self.hover(index):
            if self.colorNodes[index][0]:
                stroke(155,0,0)
                strokeWeight(2)
                fill(palette['player_colors'][index] - color(0, 0, 0, 100))
            else:
                stroke(0,155,0)
                strokeWeight(2)
                fill(palette['player_colors'][index] - color(0, 0, 0, 100))
        else:
            strokeWeight(1)
            fill(palette['player_colors'][index])
    
    def getColor(self, c):
        if c == palette['player_colors'][0]:
            return 'white'
        elif c == palette['player_colors'][1]:
            return 'black'
        elif c == palette['player_colors'][2]:
            return 'red'
        elif c == palette['player_colors'][3]:
            return 'blue'


class TextInput:

    def __init__(self, index, x, y, w = 300 ,h = 50):
        self.x = x - 80         #   X position
        self.y = y              #   Y position
        self.w = w              #   Width
        self.h = h              #   Height
        self.bevel = 6          #   Bevel
        self.padding = 15       #   Padding
        self.selected = False
        self.text = []
        self.maxLength = 15
        self.index = index
        self.forbiddenKeys = [ENTER, TAB, BACKSPACE]
        fill(palette['gray'])
        strokeCap(SQUARE)
        rectMode(CENTER)

    def draw(self):
        self.changeState('rect')
        rect(self.x, self.y, self.w, self.h, 3, 3, 0, 0)
        self.changeState('line')
        line(self.x - self.w/2, self.y + self.h/2, self.x + self.w/2, self.y + self.h/2)
        self.displayText()

    def addText(self, input):
        if self.selected == True:
            if not input in self.forbiddenKeys and len(self.text) < self.maxLength:
                self.text.append(input)
            elif input == BACKSPACE:
                self.text = self.text[:len(self.text)-1]
            elif input == ENTER and self.selected == True:
                global players
                self.selected = False
                cursor(ARROW)
                self.defineText()

    def displayText(self):
        fill(0,0,0)
        textAlign(LEFT, CENTER)
        textSize(20)
        if self.text == []:
            fill(0,0,0,100)
            text("Naam", self.x + self.padding - self.w / 2, self.y)
        else:
            fill(0,0,0)
            text(join(self.text, ""), self.x + self.padding - self.w / 2, self.y)
    
    def defineText(self):
        temp = players[self.index][0]
        players[self.index][0] = join(self.text, "")
        print('Player ' + str(self.index) + '\'s name changed\nfrom: ' + temp + '\nto: ' + str(players[self.index][0]))
    
    def hover(self):
        if f.hover([mouseX,mouseY],[self.x - self.w / 2, self.y - self.h / 2, self.w, self.h]):
            return True

    def changeState(self, type):
        if type == 'rect':
            if self.hover():
                fill(palette['gray_hover'])
            else:
                fill(palette['gray'])
            if self.selected or (self.hover() and mouseButton == LEFT):
                fill(palette['light_blue'])
                self.selected = True
                cursor(TEXT)
            if self.selected and mouseButton == LEFT and not self.hover():
                self.selected = False
                fill(palette['gray'])
                cursor(ARROW)
                self.defineText()
        elif type == 'line':
            if self.hover():
                stroke(80, 80, 80)
                strokeWeight(1)
            else:
                stroke(130,130,130)
                strokeWeight(1)
            if self.selected:
                stroke(114, 9, 183)
                strokeWeight(2)
        elif type == 'circle':
            pass
            
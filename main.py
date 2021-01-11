import invoerscherm
import puntenscherm
import eindscherm
from objects import *
import uitleg

screenSize = [1080, 720]
state = "start"

errorMsgCounter = 0
errorMsg = ""


def settings():
    if state == "start":
        size(screenSize[0], screenSize[1])


def setup():
    global state, background, toManual
    
    if state == "start":
        invoerscherm.setup()
    
    main = Screen('main', {})
    main.start()
    background = Rectangle(None, {
        'fill': '245 245 245 255',
        'w': '1080',
        'h': '720',
        'stroke': 'None'
    })
    toManual = Button(None, {
        'x': 840,
        'y': 690,
        'w': 170,
        'h': 50,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '77 107 234 255',
        'placeholder': 'Handleiding',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'font': 'OpenSans-Bold-48.vlw',
        'textColor': '255 255 255 255'
    })
    toManual.hover.setItems({
        'fill': '77 107 234 200',
        'w': 175,
        'h': 55,
        'textSize': 21
    })
    main.stop()
      
        
def draw():
    global state
    background.draw()
    
    if state == "start":
        invoerscherm.draw()
        if not invoerscherm.toNext.isSelected:
            invoerscherm.draw()
            toManual.draw()
        else:
            invoerscherm.draw()
            toManual.draw()
            if not errorHandler():
                state = "createGame"
            invoerscherm.toNext.isSelected = False
    elif state == "createGame":
        rectMode(CORNER)
        textAlign(BASELINE)
        puntenscherm.setup(invoerscherm.getNames())
        state = "preStartGame"
        
    elif state == "preStartGame":
        uitleg.draw()
        if frameCount % 500 == 0:
            state = "startGame"
        
    elif state == "startGame":
        puntenscherm.draw()
        if type(puntenscherm.dp.getAlivePlayers()) != type(0):
            if len(puntenscherm.dp.getAlivePlayers()) == 1:
                puntenscherm.toEnd.draw()
        else:
            if puntenscherm.dp.getAlivePlayers() == 1:
                puntenscherm.toEnd.draw()
        if puntenscherm.toEnd.isSelected:
            state = "endGameSetup"
        elif puntenscherm.goBack.isSelected:
            state = "start"
        font = loadFont('OpenSans-48.vlw')
        textFont(font, 16)
        
                
        puntenscherm.dp.getPlayers()
    
    elif state == "endGameSetup":	
        noTint()
        eindscherm.setup(puntenscherm.dp.getPlayers())
        cursor(ARROW)
        state = "endGame"
    elif state == "endGame":
        eindscherm.draw()

    if toManual.isSelected:
        toManual.isSelected = False

    showError()
    
def keyTyped():
    for i in range(4):
        invoerscherm.d.textInputs[i].addText(key)

    if key == TAB:
        textInputs = invoerscherm.d.textInputs
        for i in range(len(textInputs)):
            if textInputs[i].selected == True:
                textInputs[i].selected = False
                textInputs[i].defineText()
                if i + 1 > 3:
                    textInputs[0].selected = True
                else:
                    textInputs[i + 1].selected = True
                break

def showError():
    global errorMsg, errorMsgCounter
    if errorMsgCounter > 0:
        textSize(24)
        errorMsgCounter -= 1
        fill(229, 56, 59, errorMsgCounter*10)
        textAlign(CENTER)
        text(errorMsg,540,30) 	
        textAlign(LEFT)

def errorHandler():
    global errorMsg, errorMsgCounter
    if state == 'start':
        players = invoerscherm.d.players
        errorMsgCounter = invoerscherm.d.errorMsgCounter
        errorMsg = invoerscherm.d.errorMsg
        playerCount = 0
        for i in range(len(players)):
            # print(players[i][0],players[i][1],playerCount)
            if players[i][1] == 'None' and players[i][0] != '' and players[i][0] != 'None':
                errorMsgCounter = 120
                errorMsg = players[i][0] + ' does not have a color!'
                return True
            elif players[i][0] in ['', 'None'] and players[i][1] not in ['', 'None']:
                errorMsgCounter = 120
                errorMsg = players[i][1] + ' does not have a name!'
                return True
            elif players[i][0] not in ['', 'None']:
                playerCount += 1
        if playerCount < 2:
            errorMsgCounter = 120
            errorMsg = 'You need at least 2 people to play!'
            return True
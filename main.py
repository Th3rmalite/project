import invoerscherm
import puntenscherm
import eindscherm
from objects import *
import uitleg
import handleidingding as handleiding
import drawPlayers as dp

screenSize = [1080, 720]
state = "start"
previousState = state

errorMsgCounter = 0
errorMsg = ""


def settings():
    if state == "start":
        size(screenSize[0], screenSize[1])


def setup():
    global state, background, toManual1, toManual2, toNext, goBack
    
    if state == "start":
        invoerscherm.setup()
    
    main = Screen('main', {})
    main.start()
    background = Rectangle(None, {
        'fill': '225 225 225 255',
        'w': '1080',
        'h': '720',
        'stroke': 'None'
    })
    toManual1 = Button(None, {
        'x': 100,
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
    toManual1.hover.setItems({
        'fill': '77 107 234 200',
        'w': 175,
        'h': 55,
        'textSize': 21
    })
    toManual2 = Button(None, {
        'x': 240,
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
    toManual2.hover.setItems({
        'fill': '77 107 234 200',
        'w': 175,
        'h': 55,
        'textSize': 21
    })
    toNext = Button(None, {
        'x': 1000,
        'y': 690,
        'w': 130,
        'h': 50,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '67 204 37 255',
        'placeholder': 'Ga verder',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'font': 'OpenSans-Bold-48.vlw',
        'textColor': '255 255 255 255'
    })
    toNext.hover.setItems({
        'fill': '67 204 37 200',
        'w': 135,
        'h': 55,
        'textSize': 21
    })
    goBack = Button(None, {
        'x': 80,
        'y': 690,
        'w': 130,
        'h': 50,
        'stroke': '205 205 205',
        'strokeWeight': 1,
        'fill': '201 138 38 255',
        'placeholder': 'Ga terug',
        'radius': 5,
        'textSize': 20,
        'rectMode': CENTER,
        'textAlign': [CENTER, CENTER],
        'textColor': '255 255 255 255',
        'font': 'OpenSans-Bold-48.vlw'
    })
    goBack.hover.setItems({
        'fill': '201 138 38 200',
        'w': 135,
        'h': 55,
        'textSize': 21
    })
    
    main.stop()
      
        
def draw():
    global state
    background.draw()
    
    if state == "start":
        invoerscherm.draw()
        if not toNext.isSelected:
            invoerscherm.draw()
            toManual1.draw()
            toNext.draw()
        else:
            invoerscherm.draw()
            toManual1.draw()
            toNext.draw()
            if not errorHandler():
                if not mousePressed:
                    state = "createGame"
            else:
                toNext.isSelected = False

    elif state == "createGame":
        rectMode(CORNER)
        textAlign(BASELINE)
        if invoerscherm.getNames() != dp.getNames():
            puntenscherm.reset(invoerscherm.getNames())
        puntenscherm.setup()
        toNext.isSelected = False
        goBack.isSelected = False
        state = "preStartGame"
        uitleg.setup()
        
    elif state == "preStartGame":
        if not toNext.isSelected and not goBack.isSelected:
            uitleg.draw()
            toNext.draw()
            goBack.draw()
        elif toNext.isSelected:
            state = "startGame"
            toNext.isSelected = False
        elif goBack.isSelected:
            uitleg.draw()
            toNext.draw()
            goBack.draw()
            if not mousePressed:
                state = "start"
                goBack.isSelected = False
        
    elif state == "startGame":
        puntenscherm.draw()
        toManual2.draw()
        if type(puntenscherm.dp.getAlivePlayers()) != type(0):
            if len(puntenscherm.dp.getAlivePlayers()) == 1:
                puntenscherm.toEnd.draw()
        else:
            if puntenscherm.dp.getAlivePlayers() == 1:
                puntenscherm.toEnd.draw()
        if puntenscherm.toEnd.isSelected:
            state = "endGameSetup"
        elif puntenscherm.goBack.isSelected:
            if not mousePressed:
                state = "createGame"
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
        if eindscherm.playAgain.isSelected:
            invoerscherm.d.players = []
            invoerscherm.setup()
            state = "start"
    
    elif state == "manualSetup":
        handleiding.setup()
        state = "manual"
    elif state == "manual":
        handleiding.draw()
        if handleiding.goBack.isSelected:
            handleiding.draw()
            if not mousePressed:
                global previousState
                goBack.isSelected = False
                state = previousState

    if toManual1.isSelected or toManual2.isSelected:
        if not mousePressed:
            toManual1.isSelected = False
            toManual2.isSelected = False
            previousState = state
            state = "manualSetup"
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
                errorMsg = players[i][0] + ' heeft geen kleur!'
                return True
            elif players[i][0] in ['', 'None'] and players[i][1] not in ['', 'None']:
                errorMsgCounter = 120
                errorMsg = players[i][1] + ' heeft geen naam!'
                return True
            elif players[i][0] not in ['', 'None']:
                playerCount += 1
        if playerCount < 2:
            errorMsgCounter = 120
            errorMsg = 'Je hebt tenminste 2 spelers nodig verder te gaan!'
            return True
from functions import hover
import objects as obj

players = []
pawn_colors = []
cards = []
palette = obj.palette

point_worth = {
    "pawn": 1,
    "knight": 4,
    "rook": 5,
    "queen": 8,
    "king": 10
}
images = {
    "pawn": loadImage("pawn.png"),
    "knight": loadImage("knight.png"),
    "rook": loadImage("rook.png"),
    "queen": loadImage("queen.png"),
    "king": loadImage("king.png")
}

cardWidth = 1080 - 200
cardHeight = 150 - 60/4
cursorImg = ARROW
errorMsgCounter = 0
errorMsg = ""
openSans = loadFont("OpenSans-48.vlw")
openSansBold = loadFont("OpenSans-Bold-48.vlw")

def get_players(A):
    global players, pawn_colors, cardHeight, cardWidth, alivePlayers
    player_list = []
    alivePlayers = len(A)
    for i in range(len(A)):
        player_list.append(Player(A[i][0],A[i][1]))
        pawn_colors.append(A[i][1])
        
        # playercard info
        player_list[i].cardLocation = [120, 60 + (cardHeight+10)*i - 20, cardWidth, cardHeight, 5]
        
    players = player_list
    
def getAlivePlayers(): # returns list of player objects that still have their king
    return alivePlayers

def getPlayers():
    sortedList = sorted(players, key=lambda x: x.points, reverse=True)

    return sortedList
    
def get_points(target):
    global players
    
    target.points = 0
    for player in players:
        if target.player_color == player.player_color:
            pass
        else:
            for pawn in player.pawns:
                if pawn.pawn_color == target.player_color:
                    target.points += pawn.worth

def draw_player_info():
    global cardHeight, cardWidth, cursorImg, errorMsgCounter, errorMsg, alivePlayers
    #noTint()
    Blok = loadImage('Blokje.png')
    cursorImg = ARROW
    
    textSize(26)
    for idx,i in enumerate(players):
        get_points(i)
        fill(255)
        if hover([mouseX,mouseY], i.cardLocation):
            fill(248)
        rect(i.cardLocation[0], i.cardLocation[1], i.cardLocation[2], i.cardLocation[3], 7)
        noStroke()
        strokeWeight(0)
        fill(130)
        textFont(openSansBold, 28)
        text(i.name, i.cardLocation[0]+20, 80 + (cardHeight+10)*idx)
        fill(50)
        textFont(openSansBold, 20)
        text('punten:', i.cardLocation[0]+20, 135 + (cardHeight+10)*idx)
        textFont(openSans, 20)
        text(i.points, i.cardLocation[0]+130, 135 + (cardHeight+10)*idx)
        textFont(openSansBold, 20)
        text('blokkades:', i.cardLocation[0]+20, 160 + (cardHeight+10)*idx)
        test = i.points // 5

        i.change_to_pawn_color(i.pawns[-1])
        noTint()
        if test >= 1:
            image(Blok, 250, 140 + (cardHeight+10)*idx,20,20)
        if test >= 2:
            image(Blok, 270, 140 + (cardHeight+10)*idx,20,20)
        if test >= 3:
            image(Blok, 290, 140 + (cardHeight+10)*idx,20,20)
        if test >= 4:
            image(Blok, 310, 140 + (cardHeight+10)*idx,20,20)
        if test >= 5:
            image(Blok, 330, 140 + (cardHeight+10)*idx,20,20)
        
    
    for idx,player in enumerate(players):
        player.draw_pawns(idx)
        
    if not mousePressed:
        alivePlayers = []
        for player in players:
            if player.isAlive():
                alivePlayers.append(player)
        
    
    cursor(cursorImg)
    # draw error message when there is one
    if errorMsgCounter > 0:
        textSize(24)
        errorMsgCounter -= 1
        fill(229, 56, 59, errorMsgCounter*10)
        textAlign(CENTER)
        text(errorMsg,540,30) 	
        textAlign(LEFT)

class Player:
    def __init__(self, name, player_color):
        self.points = 0
        self.name = name
        self.player_color = player_color
        self.pawns = self.setup_pawns()
        self.cardLocation = []
        self.isActive = False
        cards.append(self)

        
    def add_points(self, points):
        self.points += points
        
    def setup_pawns(self):
        temp = []
        temp += ([Pawn("pawn", self.player_color) for i in range(6)])
        temp += ([Pawn("knight", self.player_color) for i in range(2)])
        temp += ([Pawn("rook", self.player_color) for i in range(2)])
        temp += ([Pawn("queen", self.player_color)])
        temp += ([Pawn("king", self.player_color)])
        return temp
    
    def change_to_pawn_color(self, pawn):
        alpha = 200
        if(pawn.pawn_color == "black"):
            fill(palette['player_colors'][1], alpha)
        elif(pawn.pawn_color == "white"):
            fill(palette['player_colors'][0], alpha)
        elif(pawn.pawn_color == "red"):
            fill(palette['player_colors'][2], alpha)
        elif(pawn.pawn_color == "blue"):
            fill(palette['player_colors'][3], alpha)
            
        if(pawn.owner_color == "black"):
            tint(palette['player_colors'][1])
        elif(pawn.owner_color == "white"):
            tint(palette['player_colors'][0])
        elif(pawn.owner_color == "red"):
            tint(palette['player_colors'][2])
        else:
            tint(palette['player_colors'][3])
    
    def isAlive(self):
        if self.pawns[-1].pawn_color == self.player_color:
            return True
        else:
            return False      
    
    def draw_pawns(self,idx):
        global pawn_colors, images, alreadyDragging, players, cursorImg, errorMsgCounter, errorMsg, alivePlayers
        mouse = [mouseX,mouseY]
        high = 0
        
        
        for i in range(len(self.pawns)):
            currentPawn = self.pawns[i]
            if i % 4 == 0 and i != 0:
                high += 1
            self.change_to_pawn_color(currentPawn)
            currentPawn.location = [1080 - 45*4 - 45*(i-(high*4)), 50+40*high + idx*145, 35, 35]

            if currentPawn.drag:
                cursorImg = MOVE
            # change color to card below
            for player in players:
                if hover(mouse, player.cardLocation) and currentPawn.drag:
                    currentPawn.pawn_color = player.player_color
                    break
            if not mousePressed:
                self.clicked = False
                currentPawn.drag = False
                alreadyDragging = False
            if hover(mouse, currentPawn.location) or currentPawn.drag:
                cursorImg = MOVE
                fill(20,0)

                if alreadyDragging or currentPawn.pawn_color == currentPawn.owner_color:
                    self.isActive = True
                    if mousePressed and not alreadyDragging and mouseButton == LEFT:
                        alreadyDragging = True
                        currentPawn.drag = True
                    if currentPawn.drag:
                        currentPawn.location = [mouseX-28, mouseY-32, 35, 35]
                else:
                    # reset color
                    cursorImg = HAND
                    if mousePressed and mouseButton == RIGHT:
                        currentPawn.pawn_color = currentPawn.owner_color
                    elif mousePressed and mouseButton == LEFT:
                        errorMsgCounter = 120
                        errorMsg = "Press right mouse button to clear color"
                    # hier moet een error msg komen als mouseButton == LEFT
                        
                # update color by clicking
                '''
                if mousePressed and (mouseButton == LEFT) and not self.clicked:
                    self.clicked = True
                    print(currentPawn.name, currentPawn.pawn_color, currentPawn.worth)
                    try:
                        currentPawn.pawn_color = pawn_colors[:len(players)][pawn_colors.index(currentPawn.pawn_color)+1]
                    except:
                        currentPawn.pawn_color = pawn_colors[0]
                '''
                
                rect(currentPawn.location[0], currentPawn.location[1], currentPawn.location[2], currentPawn.location[3], 15)
            self.change_to_pawn_color(currentPawn)
            if currentPawn.pawn_color != currentPawn.owner_color:
                rect(currentPawn.location[0], currentPawn.location[1], currentPawn.location[2], currentPawn.location[3], 15)
            image(currentPawn.img, currentPawn.location[0], currentPawn.location[1], currentPawn.location[2], currentPawn.location[3])
        
class Pawn:
    def __init__(self,type,pawn_color):
        self.drag = False
        self.imagePointer = type + ".png"
        self.img = loadImage(self.imagePointer)
        self.location = []
        self.clicked = False
        self.worth = point_worth[type]
        self.name = type
        self.pawn_color = pawn_color
        self.owner_color = pawn_color
        
    def add_to_player(self, player):
        player.add_points(self.worth)
        print(str(self.worth), player.name)

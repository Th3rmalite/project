from functions import hover

players = []
pawn_colors = []
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
    'player_colors' :   {
                        "white": color(248, 249, 250),   # white
                        "black": color(20, 23, 26),      # black
                        "red": color(164, 22, 26),     # red
                        "blue": color(3, 4, 94)         # blue
                        }
}

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

cardWidth = 1080 - 240
cardHeight = 150 - 60/4
cursorImg = ARROW

def get_players(A):
    global players, pawn_colors, cardHeight, cardWidth
    player_list = []
    
    for i in range(len(A)):
        player_list.append(Player(A[i][0],A[i][1]))
        pawn_colors.append(A[i][1])
        
        # playercard info
        player_list[i].cardLocation = [120, 60 + (cardHeight+20)*i, cardWidth, cardHeight, 5]
        
    players = player_list
    
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
    global cardHeight, cardWidth, cursorImg
    noTint()
    # Blok = loadImage('blokje (2).png')
    cursorImg = ARROW
    
    textSize(26)
    for idx,i in enumerate(players):
        get_points(i)
        fill(90)
        rect(i.cardLocation[0], i.cardLocation[1], i.cardLocation[2], i.cardLocation[3])
        fill(255)
        text(i.name, 140, 100 + (cardHeight+20)*idx)
        text(i.player_color, 140, 130 + (cardHeight+20)*idx)
        text("punten:", 140, 180 + (cardHeight+20)*idx)
        text(i.points, 250, 180 + (cardHeight+20)*idx)
        text('blokkades:', 140, 155 + (cardHeight+20)*idx)
        test = i.points // 5
        if test >= 1:
            image(Blok, 285, 138 + (cardHeight+20)*idx,20,20)
        if test >= 2:
            image(Blok, 310, 138 + (cardHeight+20)*idx,20,20)
        if test >= 3:
            image(Blok, 335, 138 + (cardHeight+20)*idx,20,20)
        if test >= 4:
            image(Blok, 360, 138 + (cardHeight+20)*idx,20,20)
        if test >= 5:
            image(Blok, 385, 138 + (cardHeight+20)*idx,20,20)
        
    for idx,player in enumerate(players):
        player.draw_pawns(idx)
    
    cursor(cursorImg)

class Player:
    def __init__(self, name, player_color):
        self.points = 0
        self.name = name
        self.player_color = player_color
        self.pawns = self.setup_pawns()
        self.cardLocation = []

        
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
        if(pawn.pawn_color == "black"):
            fill(0)
        elif(pawn.pawn_color == "white"):
            fill(255)
        elif(pawn.pawn_color == "red"):
            fill(255,0,0)
        elif(pawn.pawn_color == "blue"):
            fill(0,0,255)
            
        if(pawn.owner_color == "black"):
            tint(0)
        elif(pawn.owner_color == "white"):
            tint(255)
        elif(pawn.owner_color == "red"):
            tint(255,0,0)
        else:
            tint(0,0,255)
            
    def draw_pawns(self,idx):
        global pawn_colors, images, alreadyDragging, players, cursorImg
        mouse = [mouseX,mouseY]
        high = 0
        
        for i in range(len(self.pawns)):
            currentPawn = self.pawns[i]
            if i % 4 == 0 and i != 0:
                high += 1
            self.change_to_pawn_color(currentPawn)
            currentPawn.location = [1080 - 45*4 - 45*(i-(high*4)), 65+45*high + idx*155, 35, 35]

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
                
                rect(currentPawn.location[0], currentPawn.location[1], currentPawn.location[2], currentPawn.location[3], 3)
            self.change_to_pawn_color(currentPawn)
            if currentPawn.pawn_color != currentPawn.owner_color:
                rect(currentPawn.location[0], currentPawn.location[1], currentPawn.location[2], currentPawn.location[3], 3)
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

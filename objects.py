environment = []

# Set properties
# Get properties
# Convert % and px to correct format
# Format multiple values to work in practice

screen = {
        'w': [1280],
        'h': [720],
        'x': [0],
        'y': [0],
        'rectMode': [CORNER]
    }

class Property:
    global screen

    def __init__(self, parent = None):
        if not parent:
            self.parent = screen
        else:
            self.parent = parent

        self.default = {
                'w': 50,
                'h': 50,
                'x': 0,
                'y': 0,
                'radius': 0,
                'fill': '255 255 255 255',
                'stroke': '0 0 0',
                'strokeWeight': 1,
                'strokeCap': SQUARE,
                'rectMode': CORNER,
                'textSize': 16,
                'placeholder': '',
                'textColor': '0 0 0 255',
                'textAlign': [LEFT, BOTTOM],
                'textMargin': '0 0',
                'selectType': 'hold'
            }

        self.storage = {}

        self.setDefault()

    def setDefault(self, copyValues = True):
        """Default item duplication to property storage

        Parameters:
        bool copyValues: If false, setDefault will only export the keys to storage.
        """
        if copyValues == True:
            for propertyType in self.default.keys():
                self[propertyType] = self.default[propertyType]
        else:
            for propertyType in self.default.keys():
                self.storage.update({propertyType: ''})

    def __setitem__(self, propertyType, propertyValue):
        if propertyType in self.default.keys():
            if not isinstance(propertyValue, str):
                if isinstance(propertyValue, list):
                    self.storage[propertyType] = propertyValue
                else:
                    self.storage[propertyType] = self.setMultipleValues(propertyType, self.toNormal(propertyValue))
            else:
                self.storage[propertyType] = self.setMultipleValues(propertyType, propertyValue)
        else:
            print("'" + str(propertyType) + "' is not a valid property key!")
            

    def __getitem__(self, propertyType):
        return self.storage[propertyType]

    def setItems(self, properties):
        for propertyKey, propertyValue in properties.items():
            self[propertyKey] = propertyValue
    
    def getItems(self):
        temp = {}
        for propertyKey in self.storage.keys():
            temp[propertyKey] = self[propertyKey]
        return temp

    def setMultipleValues(self, propertyType, propertyValue):
        splitValues = propertyValue.split()
        for index in range(len(splitValues)):
            splitValues[index] = self.toReal(propertyType, splitValues[index])
        return splitValues
    
    def toReal(self, propertyType, normalValue):
        if '%'in normalValue:
            percent = float(normalValue.replace('%', '')) / 100
            if propertyType in 'wh':
                return self.parent[propertyType][0] * percent
            if self.parent['rectMode'][0] == CORNER:
                if propertyType == 'x':
                    return self.parent['x'][0] + self.parent['w'][0] * percent
                elif propertyType == 'y':
                    return self.parent['y'][0] + self.parent['h'][0] * percent
            elif self.parent['rectMode'][0] == CENTER:
                if propertyType in 'xy':
                    return self.parent[propertyType][0] + self.parent['w'][0] * percent - self.parent['w'][0] / 2
        try:
            if str(int(normalValue)).isnumeric():
                if propertyType == 'x' or propertyType == 'y':
                    return self.parent[propertyType][0] + int(normalValue)
                else:
                    return int(normalValue)
        except:
            return normalValue

    def toNormal(self, realValue):
        if isinstance(realValue, list):
            temp = []
            for i in range(len(realValue)):
                temp.append(self.toNormal(realValue[i]))
            return temp
        else:
            return str(realValue)

class Screen(object):

    def __init__(self, name, properties = None):
        self.name = name
        self.properties = Property(None)
        self.properties.setItems(properties)
        self.active = False
        self.content = []
        self.data = {}
    
    def start(self):
        global environment
        if self in environment:
            print("Error for " + str(self.name) + ": start() has already been initialized.")
        else:
            self.active = True
            environment.append(self)
    
    def stop(self):
        if self.active == False:
            print("Error for " + str(self.name) + ": you cannot initialize stop() before start().")
        else:
            self.active = False
    
    def addData(self, key, value):
        self.data[key] = value
    
    def delData(self, key):
        del self.data[key]

    def getData(self, key = False):
        if key:
            return self.data[key]
        else:
            return self.data
    
    def addContent(self, objectToAdd):
        self.content.append(objectToAdd)

    def drawContent(self):
        for i in range(len(self.content)):
            content.draw()

class Instance(object):

    def __init__(self, parent, properties = None):
        global environment
        self.parent = parent
        self.default = properties
        self.properties = Property(parent)
        self.hover = Property(parent)
        self.selected = Property(parent)
        self.hover.setItems(properties)
        self.selected.setItems(properties)
        self.properties.setItems(properties)
        self.isSelected = False
        for i in range(len(environment)):
            if environment[i].active == True:
                self.screen = environment[i]
        try:
            self.screen.content.append(self)
        except:
            print("Could not find an active screen for " + str(self))

    def __setitem__(self, propertyType, propertyValue):
        self.properties[propertyType] = propertyValue

    def __getitem__(self, propertyType):
        return self.properties[propertyType]

    def drawInstance(self):
        if self.isHover() and not self.isSelected:
            self.hoverEvent()
        elif not self.isSelected:
            self.properties.setItems(self.default)
        self.setting()
    
    def hoverEvent(self):
        self.properties.setItems(self.hover.getItems())
    
    def mousePressedEvent(self):
        self.isSelected = True
        self.properties.setItems(self.selected.getItems())
    
    def mouseReleasedEvent(self):
        self.isSelected = False
        self.properties.setItems(self.default)

    def isHover(self):
        a = [mouseX,mouseY]
        if self['rectMode'][0] == CORNER:
            b = [self['x'][0], self['y'][0], self['w'][0], self['h'][0]]
        else:
            b = [self['x'][0] - self['w'][0] / 2, self['y'][0] - self['h'][0] / 2, self['w'][0], self['h'][0]]
        isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
        isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
        if (isBetweenY and isBetweenX):
            return True
        return False


    def setting(self):
        if self['fill'][0] == 'None':
            noFill()
        else:
            fill(
                self['fill'][0],
                self['fill'][1],
                self['fill'][2],
                self['fill'][3]
            )
        if self['stroke'][0] == 'None':
            noStroke()
        else:
            stroke(
                self['stroke'][0],
                self['stroke'][1],
                self['stroke'][2]
            )
        

class Rectangle(Instance):

    def __init__(self, parent, properties = None):
        super(Rectangle, self).__init__(parent, properties)
    
    def shape(self):
        rectMode(int(self['rectMode'][0]))
        rect(
            self['x'][0],
            self['y'][0],
            self['w'][0],
            self['h'][0],
            self['radius'][0]
        )

    def draw(self):
        self.drawInstance()
        self.shape()


class Button(Rectangle):

    def __init__(self, parent, properties = None):
        super(Button, self).__init__(parent, properties)
        self.goTo = self.screen
    
    def draw(self):
        self.drawInstance()
        self.shape()

class TextField(Rectangle):

    def __init__(self, parent, properties = None):
        super(TextField, self).__init__(parent, properties)
        self.text = ''
        self.forbidden = [ENTER, TAB, BACKSPACE]
    
    def draw(self):
        self.drawInstance()
        self.shape()
        self.drawText()
    
    def drawText(self):
        fill(self['textColor'][0], self['textColor'][1], self['textColor'][2], self['textColor'][3])
        textAlign(self['textAlign'][0], self['textAlign'][1])
        textSize(self['textSize'][0])
        if not self.isSelected and self.text == '':
            text(self['placeholder'][0], self['x'][0] + self['textMargin'][0], self['y'][0] + self['textMargin'][1] + self['h'][0] / 2, self['textMargin'][1])
        else:
            text(self.text, self['x'][0] + self['textMargin'][0], self['y'][0], self['textMargin'][1])


    
    def keyTypedEvent(self):
        pass
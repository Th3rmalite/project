environment = []

# Set properties
# Get properties
# Convert % and px to correct format
# Format multiple values to work in practice


screen = {
        'w': 1280,
        'h': 720
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
                'fill': '0 0 0 255',
                'stroke': '0 0 0',
                'rectMode': CORNER
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
                self.storage[propertyType] = self.setMultipleValues(propertyType, self.toNormal(propertyValue))
            else:
                self.storage[propertyType] = self.setMultipleValues(propertyType, propertyValue)
        else:
            print("'" + str(propertyType) + "' is not a valid property key!")
            

    def __getitem__(self, propertyType, realValue = True):
        if realValue == True:
            try:
                return self.toReal(propertyType, self.storage[propertyType])
            except:
                return None
        else:
            return self.storage[propertyType]

    def setItems(self, properties):
        for propertyKey, propertyType in properties.items():
            self[propertyKey] = propertyType
    
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
        if 'px' in normalValue:
            return int(float(normalValue.replace('px', '')))
        elif '%' in normalValue:
            percentageToPixels = int(self.parent[propertyType] * (float(normalValue.replace('%', '')) / 100))
            return self.toReal(propertyType, self.toNormal(percentageToPixels))
        else:
            if isinstance(normalValue, list):
                temp = []
                for i in range(len(normalValue)):
                    temp.append(self.toReal(propertyType, self.toNormal(normalValue[i])))
                return temp
            else:
                try:
                    if isinstance(float(normalValue), float):
                        return self.toReal(propertyType, self.toNormal(normalValue))
                except:
                    return normalValue

    def toNormal(self, realValue):
        try:
            return str(float(realValue)) + 'px'
        except:
            if isinstance(realValue, list):
                temp = []
                for i in range(len(realValue)):
                    temp.append(self.toNormal(realValue[i]))
                return temp
            else:
                return realValue

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
        self.properties = Property(parent)
        self.properties.setItems(properties)
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
        self.setting()

    def hover(self):
        a = [mouseX,mouseY]
        b = [self['x'][0], self['y'][0], self['w'][0], self['h'][0]]
        isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
        isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
        if (isBetweenY and isBetweenX):
            return True
        return False

    def click(self):
        pass

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
            self['h'][0]
        )

    def draw(self):
        self.drawInstance()
        self.shape()

class Button(Rectangle):

    def __init__(self, parent, properties = None):
        super(Button, self).__init__(parent, properties)
        self.goTo = self.screen
        self.selected = False
    
    def draw(self):
        if self.hover() and not self.selected:
            self['fill'] = '230 100 10 255'
        else:
            self['fill'] = '100 50 50 255'
        self.drawInstance()
        self.shape()
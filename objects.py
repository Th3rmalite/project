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
                'fill': '0 0 255'
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
            return self.toReal(propertyType, self.storage[propertyType])
        else:
            return self.storage[propertyType]

    def setProperties(self, properties):
        for propertyKey, propertyType in properties.items():
            self[propertyKey] = propertyType
    
    def getProperties(self):
        temp = {}
        for propertyKey in self.storage.keys():
            temp[propertyKey] = str(self[propertyKey])
        return temp

    def setMultipleValues(self, propertyType, propertyValue):
        splitValues = propertyValue.split()
        for index in range(len(splitValues)):
            splitValues[index] = self.toReal(propertyType, splitValues[index])
        return splitValues

    def toReal(self, propertyType, normalValue):
        if 'px' in normalValue:
            return int(normalValue.replace('px', ''))
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
                return self.toReal(propertyType, self.toNormal(normalValue))

    def toNormal(self, realValue):
        try:
            return str(int(realValue)) + 'px'
        except:
            if isinstance(realValue, list):
                temp = []
                for i in range(len(realValue)):
                    temp.append(self.toNormal(realValue[i]))
                return temp
            print('Could not turn ' + str(realValue) + ' into normal value. The value is probably not a number.')

class Screen(object):

    def __init__(self, name, properties = None):
        self.name = name
        self.properties = Property(None)
        self.properties.setProperties(properties)
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
            quit()
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
        self.properties.setProperties(properties)
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

    def draw(self):
        pass

    def onHover(self):
        pass

    def onClick(self):
        pass

class Rectangle(Instance):
    pass
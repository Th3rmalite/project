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
                'w': '50%',
                'h': '50px',
                'x': 0,
                'y': 0
            }

        self.storage = {}

        self.setDefault()

    def setDefault(self, copyValues = True):
        if copyValues == True:
            self.storage = self.default
        else:
            for propertyType in self.default.keys():
                self.storage.update({propertyType: ''})

    def __setitem__(self, propertyType, propertyValue):
        if propertyType in self.default.keys():
            if not isinstance(propertyValue, str):
                self.storage[propertyType] = self.toNormal(propertyValue)
            else:
                self.storage[propertyType] = propertyValue
        else:
            print("'" + str(propertyType) + "' is not a valid property key!")
            

    def __getitem__(self, propertyType, realValue = False):
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

    def setMultipleItems(self):
        pass

    def toReal(self, propertyType, normalValue):
        if isinstance(normalValue, int):
            return self.toReal(propertyType, self.toNormal(normalValue))
        elif 'px' in normalValue:
            return int(normalValue.replace('px', ''))
        elif '%' in normalValue:
            percentageToPixels = int(self.parent[propertyType] * (float(normalValue.replace('%', '')) / 100))
            return self.toReal(propertyType, self.toNormal(percentageToPixels))

    def toNormal(self, realValue):
        try:
            return str(int(realValue)) + 'px'
        except:
            print('Could not turn ' + str(realValue) + ' into normal value. Probably because the value is not a number.')

class FormObject(object):
    global screen

    def __init__(self, parent, properties):
        self.properties = Property(parent)
        self.properties.setProperties(properties)

    def __setitem__(self, propertyType, propertyValue):
        self.properties[propertyType] = propertyValue

    def __getitem__(self, propertyType):
        return self.properties[propertyType]

    def onHover(self):
        pass

    def onClick(self):
        pass

class Screen:

    def __init__(self, properties = None):
        self.properties = Property(None)
        self.properties.setProperties(properties)
        self.content = {}
    
    def addContent(self, key, value):
        self.content[key] = value
    
    def delContent(self, key):
        del self.content[key]

    def __getitem__(self, key):
        return self.content[key]
Screen = {'width': 1280, 'height': 720, 'x': 0, 'y': 0}
screenSize = [1280, 720]

content = []

class Properties:

    def __init__(self, parent):
        global Screen
        if not parent:
            self.parent = Screen
        else:
            self.parent = parent

        self.default = {
            'width': '50px',
            'height': '50px',
            'color': color(0,0,0),
            'background-color': color(255,255,255),
            'x': '0px',
            'y': '0px',

            'border': '1px',
            'border-color': color(0,0,0), 

            'radius': '0px',

            'inherit': 'absolute',
            'text-align': 'left',
            'vertical-align': 'top',
            'rect-align': CORNER,
            
            'box-shadow': 'none',
            'shadow-color': color(0,0,0,2)
        }

        self.get = self.default

        for key, value in self.default.items():
            if isinstance(value, str):
                try:
                    self.default[key] = self.multipleValues(key, value)
                except:
                    print('<An error has occured> ' + key + ' : ' + value)
            else:
                self.default[key] = value
        
        self.get = self.default
    
    def __getitem__(self, key):
        '''
        Returns the table with all current Properties for the object.
        '''
        return self.get[key]

    def __setitem__(self, key, value):
        '''
        Change the Properties of an object easily:
            <objName>[keyName] = value
            table['height'] = '50px'
        '''
        if key in self.get:
            try:
                if isinstance(value, str):
                    self.get[key] = self.multipleValues(key, value)
                else:
                    self.get[key] = value
            except:
                print(str(value) + ' is not a valid value for ' + str(key) + '.\nWill use default value of ' + str(self.default[key]) + ' instead.\n')
        else:
            print(str(key) + ' does not exist in Propertiess.\n')

    def multipleValues(self, key, string):
        '''
        If the string contains multiple values (ex: 'padding': '2px 1px 5px 10px'), return a string with the correct values.
        '''
        lis = string.split(' ')
        newValue = {}

        for index in range(len(lis)):
            lis[index] = self.formatForCalculations(key, lis[index])
        
        if key == 'box-shadow':
            if len(lis) == 1:
                return 'none'
            elif len(lis) == 2:
                newValue = {
                    'offset-x' : lis[0],
                    'offset-y' : lis[1],
                    'spread' : 0
                }
            elif len(lis) == 3:
                newValue = {
                    'offset-x' : lis[0],
                    'offset-y' : lis[1],
                    'spread' : lis[2]
                }
        else:
            if len(lis) == 1:
                if key != 'radius':
                    return lis[0]
                else:
                    newValue = {
                        'left' : lis[0],
                        'top' : lis[0],
                        'right' : lis[0],
                        'bottom' : lis[0]
                    }
            elif len(lis) == 2:
                newValue = {
                        'left' : lis[0],
                        'top' : lis[1],
                        'right' : lis[0],
                        'bottom' : lis[1]
                    }
            elif len(lis) == 4:
                newValue = {
                        'left' : lis[0],
                        'top' : lis[1],
                        'right' : lis[2],
                        'bottom' : lis[3]
                    }
        
        return newValue

    
    def formatForCalculations(self, key, string):
        '''
        Convert percentages and pixels to numbers that can be used for calculations.

        Returns a ValueError when the string doesn't match either.
        '''
        temp = ''
        for character in string:
            if character.isnumeric():
                temp += character
            else:
                if '%' in string:
                    t = floor(self.keyFormat(key, float(temp)))
                    return t
                elif 'px' in string:
                    return self.otherKeyFormat(key, temp)
        return string
        
    def keyFormat(self, key, value):
        '''
        Division for percentages.
        '''
        if self['inherit'] == 'absolute':
            if key == 'width' or key == 'x':
                return Screen['width'] * (value/100)
            elif key == 'height' or key == 'y':
                return Screen['height'] * (value/100)
        elif self['inherit'] == 'relative':
            if key == 'width':
                return self.parent['width'] * (value/100)
            elif key == 'height':
                return self.parent['height'] * (value/100)
            if self.parent['rect-align'] == CORNER:
                if key == 'x':
                    return self.parent['x'] + self.parent['width'] * (value/100)
                elif key == 'y':
                    return self.parent['y'] + self.parent['height'] * (value/100)
            elif self.parent['rect-align'] == CENTER:
                if key == 'x':
                    return self.parent['x'] + self.parent['width'] * (value/100) - self.parent['width'] / 2
                elif key == 'y':
                    return self.parent['y'] + self.parent['height'] * (value/100) - self.parent['height'] / 2
 
    def otherKeyFormat(self, key, value):
        if self['inherit'] == 'absolute':
            return int(value)
        elif self['inherit'] == 'relative':
            if self.parent['rect-align'] == CORNER:
                if key == 'x':
                    return self.parent['x'] + int(value)
                elif key == 'y':
                    return self.parent['y'] + int(value)
            else:
                if key == 'x':
                    return self.parent['x'] - self.parent['width'] / 2 + int(value)
                elif key == 'y':
                    return self.parent['y'] - self.parent['height'] / 2 + int(value)

class formObject(object):
    
    def __init__(self, parent, dictionary):
        self.properties = Properties(parent)

        for key, value in dictionary.items():
            self[key] = value
        
        self.parent = parent
        global content
        content.append(self)
    
    def __setitem__(self, key, value):
        self.properties[key] = value
    
    def __getitem__(self, key):
        return self.properties[key]

    def drawShadow(self):
        if self['box-shadow'] != 'none':
            if self['rect-align'] == CORNER:
                rectMode(CENTER)
                noStroke()
                fill(self['shadow-color'])
                for i in range(120):
                    rect(
                        (self['x'] + self['width'] / 2) + self['box-shadow']['offset-x'],
                        (self['y'] + self['height'] / 2) + self['box-shadow']['offset-y'],
                        self['width'] - i * .5 + self['box-shadow']['spread'],
                        self['height'] - i * .5 + self['box-shadow']['spread'],
                        self['radius']['left'] + 5,
                        self['radius']['top'] + 5,
                        self['radius']['right'] + 5,
                        self['radius']['bottom'] + 5
                        )
            elif self['rect-align'] == CENTER:
                rectMode(CENTER)
                noStroke()
                fill(self['shadow-color'])
                for i in range(120):
                    rect(
                        self['x'] + self['box-shadow']['offset-x'],
                        self['y'] + self['box-shadow']['offset-y'],
                        self['width'] - i * .5 + self['box-shadow']['spread'],
                        self['height'] - i * .5 + self['box-shadow']['spread'],
                        self['radius']['left'] + 5,
                        self['radius']['top'] + 5,
                        self['radius']['right'] + 5,
                        self['radius']['bottom'] + 5
                        )


class Rectangle(formObject):

    def __init__(self, parent, dictionary):
        formObject.__init__(self, parent, dictionary)

    
    def draw(self):
        if self['border'] == 0:
            noStroke()
        else:
            strokeWeight(self['border'])
            stroke(self['border-color'])
        fill(self['background-color'])
        rectMode(self['rect-align'])
        rect(self['x'], self['y'], self['width'], self['height'], self['radius']['left'], self['radius']['top'], self['radius']['right'], self['radius']['bottom'])

class Table(formObject):

    def __init__(self, parent, dictionary):
        formObject.__init__(self, parent, dictionary)
    
    
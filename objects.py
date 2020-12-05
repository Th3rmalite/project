Screen = {'width': 1280, 'height': 720, 'x': 0, 'y': 0}
screenSize = [1280, 720]

class Properties:

    def __init__(self, content, parent):
        global Screen
        self.content = content
        if not parent:
            self.parent = Screen
        else:
            self.parent = parent

        self.default = {
            'width': '50%',
            'height': '100%',
            'color': color(0,0,0),
            'background-color': color(255,255,255),
            'x': '0px',
            'y': '0px',

            'margin': '1px',

            'border': '1px',
            'border-color': color(0,0,0), 
            
            'padding': '1px',

            'radius': '0px',

            'inherit': 'absolute'
        }

        self.get = self.default

        for key, value in self.default.items():
            if isinstance(value, str):
                try:
                    self.default[key] = self.formatForCalculations(key, value)
                except:
                    print('<An error has occured> ' + key + ' : ' + value)
        
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
        newValue = {'left': '',
                    'top': '',
                    'right': '',
                    'bottom': ''}

        for index in range(len(lis)):
            lis[index] = self.formatForCalculations(key, lis[index])
        

        if len(lis) == 1:
            return lis[0]
        elif len(lis) == 2:
            newValue['left'] = lis[0]
            newValue['right'] = lis[0]
            newValue['top'] = lis[1]
            newValue['bottom'] = lis[1]
        elif len(lis) == 4:
            newValue['left'] = lis[0]
            newValue['right'] = lis[1]
            newValue['top'] = lis[2]
            newValue['bottom'] = lis[3]
        else:
            raise ValueError
        
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

    def otherKeyFormat(self, key, value):
        if self['inherit'] == 'absolute':
            return int(value)
        else:
            if key == 'x':
                return self.parent['x'] + int(value)
            elif key == 'y':
                return self.parent['y'] + int(value)

class Rectangle:

    def __init__(self, parent, dictionary, content = False):
        self.properties = Properties(content, parent)

        for key, value in dictionary.items():
            self[key] = value

        self.content = content
        self.parent = parent

    def __setitem__(self, key, value):
        self.properties[key] = value

    def __getitem__(self, key):
        return self.properties[key]
    
    def draw(self):
        strokeWeight(self['border'])
        stroke(self['border-color'])
        fill(self['background-color'])
        rect(self['x'], self['y'], self['width'], self['height'], self['radius'])
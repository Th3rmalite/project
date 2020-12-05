screenSize = [1280, 720]

class Attribute:

    def __init__(self):

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
        }

        for key, value in self.default.items():
            if isinstance(value, str):
                self.default[key] = self.formatForCalculations(key, value)
        
        self.get = self.default
    
    def __getitem__(self, key):
        '''
        Returns the table with all current attributes for the object.
        '''
        return self.get[key]

    def __setitem__(self, key, value):
        '''
        Change the attribute of an object easily:
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
            print(str(key) + ' does not exist in Attributes.\n')

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
                    return int(temp)
        return string
        
    def keyFormat(self, key, value):
        '''
        Division for percentages.
        '''
        if key == 'width' or key == 'x':
            return screenSize[0] * (value/100)
        elif key == 'height' or key == 'y':
            return screenSize[1] * (value/100)

class Rectangle:

    def __init__(self, dictionary):
        self.attribute = Attribute()

        for key, value in dictionary.items():
            self[key] = value

    def __setitem__(self, key, value):
        self.attribute[key] = value

    def __getitem__(self, key):
        return self.attribute[key]
    
    def draw(self):
        strokeWeight(self['border'])
        stroke(self['border-color'])
        fill(self['background-color'])
        rect(self['x'], self['y'], self['width'], self['height'], self['radius'])

class Table:

    def __init__(self, dictionary):
        self.attribute = Attribute()

        for key, value in dictionary.items():
            self[key] = value

    def __setitem__(self, key, value):
        self.attribute[key] = value

    def __getitem__(self, key):
        return self.attribute[key]
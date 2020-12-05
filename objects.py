screenSize = [1280, 720]

class Attribute:

    def __init__(self):
        self.default = {
            'border': '1px',
            'width': '50%',
            'height': '100%',
            'color': color(0,0,0),
            'x': '',
            'y': ''
        }

        for key, value in self.default.items():
            if isinstance(value, str):
                self.default[key] = self.formatConvert(key, value)
        
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
                    self.get[key] = self.formatConvert(key, value)
                else:
                    self.get[key] = value
            except:
                print(str(value) + ' is not a valid value for ' + str(key) + '.\nWill use default value of ' + str(self.default[key]) + ' instead.\n')
        else:
            print(str(key) + ' does not exist in Attributes.\n')
    
    def formatConvert(self, key, string):
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
                else:
                    return ValueError
        return string
        
    def keyFormat(self, key, value):
        '''
        Division for percentages.
        '''
        if key == 'width' or key == 'x':
            return screenSize[0] * (value/100)
        elif key == 'height' or key == 'y':
            return screenSize[1] * (value/100)

class Table:

    def __init__(self, dictionary):
        self.attribute = Attribute()

        for key, value in dictionary.items():
            self[key] = value

    def __setitem__(self, key, value):
        self.attribute[key] = value
    
    def __getitem__(self, key):
        return self.attribute[key]
    
    def draw(self):
        fill(self['color'])
        rect(self['x'], self['y'], self['width'], self['height'])
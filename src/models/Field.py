class Field(object):
    def __init__(self, _width, _height, _surface):
        self.width = _width
        self.height = _height
        self.surface = _surface
        
    def __str__(self):
        return 'Field : [ w:' + self.width  + ' h: '+ self.height + ' surface '+ self.surface +']'
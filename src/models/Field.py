from ..utils.enum import Enum

Surface = Enum(["SAND", "GRASS", "CONCRETE"]) 

class Field(object):
    def __init__(self, _width, _height, _surface=Surface.SAND):
        self.width = _width
        self.height = _height
        self.surface = _surface
        
    def __str__(self):
        return 'Field : [ w:' + self.width  + ' h: '+ self.height + ' surface '+ self.surface +']'

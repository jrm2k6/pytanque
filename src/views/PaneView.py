from pygame import Surface

class Pane(object):
    def __init__(self, _width, _height, _display):
        self.width = _width
        self.height = _height
        self.display = _display
    
    @property
    def display(self):
        return self.display
    
    def displayPane(self):
        surface = Surface((self.width, self.height))
        surface.fill(255, 0, 0)
        Surface.blit(surface, self.display)
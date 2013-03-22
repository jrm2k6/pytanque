class BallView(object):
    def __init__(self, _color, _size):
        self.color = _color
        self.size = _size
    
    @property
    def color(self):
        return self.color
    
    @property
    def size(self):
        return self.size
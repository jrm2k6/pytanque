import gtk

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.connect('destroy', gtk.main_quit)
        self.set_size_request(300, 300)
        self.set_title("La petanque")
        self.set_position(gtk.WIN_POS_CENTER)
        self.show()


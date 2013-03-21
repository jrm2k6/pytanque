class Player(object):
    def __init__(self, nickname=""):
        self.nickname = nickname
    
    def team(self, team_number):
        self.team = team_number
        
    def __str__(self):
        return 'Player : '+ self.nickname
    
        
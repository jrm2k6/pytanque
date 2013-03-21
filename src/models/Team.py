class AlreadyFullTeam(Exception):
    def __init__(self, message):
        super(AlreadyFullTeam, self).__init__()
        self.message = "Team already complete"

    def __str__(self):
        return repr(self.message)

class Team(object):

    NUM_MAX_PLAYER = 2
    
    def __init__(self, players=[]):
        self.players = players
    
    def add_player(self, player):
        if len(self.players) < self.NUM_MAX_PLAYER:
            self.players.append(player)
        else:
            raise AlreadyFullTeam("")
    
    def __str__(self):
        return 'Team : [ ' + ', '.join(str(x) for x in self.players) + ' ]' 
        
        
        
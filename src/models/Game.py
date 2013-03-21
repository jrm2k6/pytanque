import math

class Score(object):
    def __init__(self, nb_teams_playing, winning_score=13):
        self.winning_score = winning_score
        self.nb_teams_playing = nb_teams_playing
        self.scores = [0] * nb_teams_playing
        
    def __str__(self):
        return 'Scores : [ ' + ','.join(str(x) for x in self.scores) + ']'
    
    def add_points(self, nb_points, num_team):
        if num_team <= self.nb_teams_playing:
            self.scores[num_team - 1] += nb_points
        print self.scores
            
    
    def check_for_win(self, num_team, nb_points):
        if nb_points >= self.winning_score:
            if self.no_close_team(num_team - 1):
                self.show_win_message(num_team)
            else:
                pass
        else:
            pass
        
    def no_close_team(self, num_team):
        if num_team == 0:
            list_to_check = self.scores[1:]
        elif num_team == (len(self.scores)):
            list_to_check = self.scores[0: num_team -2] 
        else:
            list_to_check = self.scores[0: num_team] + self.scores[num_team:]
        
        print list_to_check
        result = True
        for elem in list_to_check:
            if math.fabs(elem - self.scores[num_team]) < 2:
                result = False
        
        return result 
    
    def show_win_message(self, num_team):
        return "Congrats " + num_team +', you won the game'
    
    
class Shoot(object):
    def __init__(self, angle, strength):
        self.angle = angle
        self.strength = strength
        
        
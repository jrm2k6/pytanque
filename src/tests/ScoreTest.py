from ..models.Game import Score
from ..models.Player import Player
from ..models.Team import Team, AlreadyFullTeam
import unittest


class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Player('Jeremy')
        self.p2 = Player('Marcel')
        
    def tearDown(self):
        pass

    def testNoPlayerAddedIfTeamAlreadyFull(self):
        np = Player('Jean-Claude')
        self.t1 = Team([self.p1, self.p2])
        self.t1.add_player(np)
        self.assertRaises(AlreadyFullTeam, self.t1.getName)

    
    def testPlayerAddedIfTeamNotFull(self):
        self.t1 = Team([self.p1])
        np = Player('Jean-Claude')
        self.t1.add_player(np)
        self.assertTrue(len(self.t1.players), 2)
        
    def testGameOverIfTeamIsFarAhead(self):
        score = Score(2, 13)
        score.add_points(13, 1)
        self.assertTrue(score.no_close_team(0))
    
    def testGameNotOverIfTeamIsCloselyFollowed(self):
        score = Score(2, 13)
        score.add_points(13, 1)
        score.add_points(12, 2)
        self.assertTrue(score.no_close_team(0))
        
    def testGameOverIfTeamNotFollowedButScoreAboveLimit(self):
        score = Score(2, 13)
        score.add_points(15, 1)
        score.add_points(13, 2)
        self.assertTrue(score.no_close_team(0))
    
        
if __name__ == "__main__":
    unittest.main()

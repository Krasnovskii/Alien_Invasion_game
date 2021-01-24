class GameStats:
    '''Track snanistics for Alien Invasion'''

    def __init__(self, ai_game):
        '''Initailize statistic'''
        self.settings = ai_game.settings
        self.reset_status()


        # High score should never be reset
        self.high_score = 0

        # Start Alien Invasion in an active state
        self.game_active = False

    def reset_status(self):
        '''Initiliaze statistics that can change during game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

class Settings:
    # Store all classes
    def __init__(self):
        '''Initialie the game's statistic settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed = 2
        self.ship_limit = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # How quickly speed up
        self.speedup_sale = 1.2
        # How quickly the game speeds up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change troughout the game'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet sirection of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        '''Increase speed settings and alien point value'''
        self.ship_speed *= self.speedup_sale
        self.bullet_speed *= self.speedup_sale
        self.alien_speed *= self.speedup_sale

        self.alien_points = int(self.alien_points * self.score_scale)









class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Intialize the game's settings"""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,255,0)
        self.bullets_allowed = 6

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
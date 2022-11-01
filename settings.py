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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,255,0)
        self.bullets_allowed = 100
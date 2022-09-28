class Settings():
    # Store all settings

    def __init__(self):
        # Screen settings
        self.screen_size_scale = 9.0 / 19.5  # width / height
        self.screen_height = 1200
        self.screen_size = (self.screen_size_scale * self.screen_height, self.screen_height)
        self.bg_color = (230, 230, 230)

        # FPS
        self.FPS = 60.0

        # gravity acceleration
        self.gravity_acceleration = 1500

        # Bird flap velocity
        self.bird_flap_velocity = -600.0
        self.bird_max_vely = 1000.0



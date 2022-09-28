import pygame

class Bird():

    def __init__(self, fb_settings, screen, clock):
        self.screen = screen

        # Initialize bird image and get its external rectangle
        self.image = pygame.image.load('images/bird.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.fb_settings = fb_settings
        self.clock = clock
        self.vely = 0
        self.alive = True

        # Place the bird at left mid of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.fb_settings.screen_size[0] / 4
        self.center = self.rect.centery

    def blit(self):
        # Make bird visible
        self.screen.blit(self.image, self.rect)

    def flap(self):
        # flapping flapping
        self.vely = self.fb_settings.bird_flap_velocity

    def update(self):
        # Move bird on y-axis, update velocity-y
        if self.vely >= 0 and self.rect.bottom <= self.fb_settings.screen_height:
            self.center += self.vely / self.fb_settings.FPS
            self.vely += self.fb_settings.gravity_acceleration / self.fb_settings.FPS
        elif self.vely <= 0 and self.rect.top >= 0:
            self.center += self.vely / self.fb_settings.FPS
            self.vely += self.fb_settings.gravity_acceleration / self.fb_settings.FPS
        self.rect.centery = self.center
        self.vely = min(self.vely, self.fb_settings.bird_max_vely)

import sys

import pygame

from settings import Settings
from bird import Bird
import game_functions as gfun


def run_game():
    # Initialize settings
    fb_settings = Settings()

    # initialize the game
    pygame.init()
    screen = pygame.display.set_mode(fb_settings.screen_size)
    pygame.display.set_caption("Flappy Bird")

    # Initialize objects
    clock = pygame.time.Clock()
    bird = Bird(fb_settings, screen, clock)
    i = 0

    # Game main loop
    while True:

        # Set FPS
        clock.tick(fb_settings.FPS)
        gfun.check_events(bird)
        bird.update()
        gfun.update_screen(fb_settings, screen, bird)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

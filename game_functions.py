import sys

import pygame


def check_events(bird):
    # Monitoring keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                bird.flap()


def update_screen(fb_settings, screen, bird):
    # Update screen and switch to new screen
    # Refresh screen for each loop
    screen.fill(fb_settings.bg_color)
    bird.blit()

    # Make the latest screen visible
    pygame.display.flip()

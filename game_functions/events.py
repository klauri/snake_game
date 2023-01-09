import sys
from time import sleep

import pygame

def check_keydown_events(event, settings, screen):
    pass

def check_keyup_events(event, settings, screen):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_events(settings, screen, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
            if play_button_clicked: start_game(settings, screen)

def start_game(settings, screen):
    pygame.mouse.set_visible(False)

    # Reset game stats

    
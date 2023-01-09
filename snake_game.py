import pygame

from Settings import Settings
from game_stats import GameStats

from display_elements.Button import Button
from sprite_classes.snake import Snake
from game_functions import events, display

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    )
    pygame.display.set_caption('Snake')

    # Make play button
    play_button = Button(settings, screen, 'Play')

    # Init stats and scoreboard
    stats = GameStats(settings)

    # Create inital Game Objects
    snake = Snake(settings, screen)

    # Load first map

    # Start game loop
    while True:
        # Listen for events
        events.check_events(settings, screen, play_button)

        display.update_screen(settings, screen, stats, play_button, snake)


if __name__ == '__main__':
    run_game()
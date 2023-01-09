import pygame

def update_screen(settings, screen, stats, play_button, snake):
    """Update images on screen and flip to the new screen"""
    screen.fill(settings.BG_COLOR)

    if not stats.active: play_button.draw_button()

    snake.blitme()
    

    pygame.display.flip()
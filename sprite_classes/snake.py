import pygame
from Settings import Settings

class Snake:
    def __init__(self, settings: Settings, screen):
        self.screen = screen
        self.settings = settings

        # Load snake image
        self.image = pygame.image.load(settings.IMG_SNAKE_PATH)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start snake at bottom right of screen
        self.rect.centerx = self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom

        # Store the value of snake head center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the snake head position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.SNAKE_SPEED_FACTOR
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.SNAKE_SPEED_FACTOR

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the snake at current location"""
        self.screen.blit(self.image, self.rect)

    def reset_pos(self):
        """Reset the snake position"""
        self.center = self.screen_rect.right
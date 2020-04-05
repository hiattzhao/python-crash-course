import pygame

class Ship():
  def __init__(self, ai_settings, screen):
    """Initialize the ship and its starting point"""
    self.screen = screen
    self.ai_settings = ai_settings

    #load the ship and its rect
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    #start ship at bottom of screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    #store decimal value for ship's center
    self.center = float(self.rect.centerx)

    #movement flags
    self.moving_right = False
    self.moving_left = False

  def update(self):
    """Update ship's position"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed_factor

    if self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed_factor

    #update rect object from self.center
    self.rect.centerx = self.center

  def blitme(self):
    """draw the ship at its current location"""
    self.screen.blit(self.image, self.rect)
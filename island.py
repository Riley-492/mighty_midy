import pygame
from pygame.sprite import Sprite

class Island(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((128, 128))
        self.image.blit(pygame.image.load("assets/water_tile.png"), (0, 0))
        self.image.blit(pygame.image.load("assets/top_left.png"), (0, 0))

        self.image.blit(pygame.image.load("assets/water_tile.png"), (64, 0))
        self.image.blit(pygame.image.load("assets/top_right.png"), (64, 0))

        self.image.blit(pygame.image.load("assets/water_tile.png"), (0, 64))
        self.image.blit(pygame.image.load("assets/bottom_left.png"), (0, 64))

        self.image.blit(pygame.image.load("assets/water_tile.png"), (64, 64))
        self.image.blit(pygame.image.load("assets/bottom_right.png"), (64, 64))
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)

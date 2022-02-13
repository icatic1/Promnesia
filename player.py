import pygame.image
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "sPlayer.jpg"))
        self.image = pygame.transform.scale(self.image, (32, 64))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)

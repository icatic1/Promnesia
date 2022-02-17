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

        # kretanje
        self.direction = pygame.math.Vector2(0, 0)
        self.player_speed = 4
        self.gravity = 0.4
        self.jump = -8

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.add_jump()

    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def add_jump(self):
        self.direction.y = self.jump


    def update(self):
        self.get_input()


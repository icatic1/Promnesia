import pygame
import constants as C
import os


def main():
    background_colour = C.WHITE
    (width, height) = (C.WIDTH, C.HEIGHT)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Promnesia')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

import pygame, sys
from settings import *
from levels import Level
import os


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Promnesia')

    # screen.blit(P.Player, (10, 0))

    clock = pygame.time.Clock()
    # pygame.display.flip()
    level = Level(MAP,screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        level.run()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

import pygame
from blocks import Block
from settings import BLOCK_SIZE


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)

    def setup(self,layout):
        self.blocks = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                if col == 'X':
                    b = Block((col_index*BLOCK_SIZE,row_index*BLOCK_SIZE),BLOCK_SIZE)
                    self.blocks.add(b)



    def run(self):
        self.blocks.draw(self.display_surface)
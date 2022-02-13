import pygame
from blocks import Block
from player import Player
from settings import BLOCK_SIZE


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)
        self.world_shift = 0

    def setup(self, layout):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # prolaz kroz string i dodavanje u grupe
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == 'X':
                    b = Block((col_index * BLOCK_SIZE, row_index * BLOCK_SIZE), BLOCK_SIZE)
                    self.blocks.add(b)
                elif col == 'P':
                    p = Player((col_index * BLOCK_SIZE, row_index * BLOCK_SIZE))
                    self.player.add(p)

    def run(self):
        # crtam platforme
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.display_surface)

        # crtam igraca
        self.player.draw(self.display_surface)

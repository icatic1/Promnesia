import pygame
from blocks import Block
from player import Player
from settings import BLOCK_SIZE,WIDTH


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

    def scroll_x(self):
        player = self.player.sprite
        player_pos = player.rect.centerx
        vector_dir = player.direction.x

        if player_pos < WIDTH/4 and vector_dir < 0:
            self.world_shift = 4
            player.player_speed = 0
        elif player_pos > WIDTH - WIDTH/4 and vector_dir > 0:
            self.world_shift = -4
            player.player_speed = 0
        else:
            self.world_shift = 0
            player.player_speed = 4

    def run(self):
        # crtam platforme
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.display_surface)

        # crtam igraca
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()

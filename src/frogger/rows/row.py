import pygame

from .. import config, graphics
from ..entities.water_transport import WaterTransport


class Row:
    def __init__(self, pos_y, width, height, tile_name):
        self.rect = pygame.Rect(0, pos_y, width, height)
        self.tile_image = graphics.load_image(
            config.DECORS_PATH / tile_name,
            (config.CELL_SIZE, self.rect.height),
        )

    def draw_background(self, screen):
        graphics.draw_debug_rect(screen, self.rect, (0, 0, 255))

        for col in range(config.COLS):
            screen.blit(self.tile_image, (col * config.CELL_SIZE, self.rect.y))

    def draw_objects(self, screen):
        pass  # par défaut, une rangée n'a pas d'objet à dessiner

    def update(self, dt):
        pass  # par défaut, une rangée ne bouge pas

    def is_deadly_for(self, _frog) -> bool:
        return False

    def find_support(self, _frog) -> WaterTransport | None:
        return None  # par défaut, rien ne porte la grenouille

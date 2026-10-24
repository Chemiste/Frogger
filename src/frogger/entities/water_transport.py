import pygame

from .. import config, graphics
from ..enums.direction_row import DirectionRow


class WaterTransport:
    def __init__(
        self,
        start_x: int,
        y: int,
        direction: DirectionRow,
        image: str,
        vehicle_length: int,
    ):
        self.pos_x = float(start_x)
        self.delta_x = 0
        self.direction = direction

        width = config.CELL_SIZE * vehicle_length
        self.image = graphics.load_image_with_width(config.RIVER_PATH / image, width)

        height = self.image.get_height()
        offset = (config.CELL_SIZE - height) // 2
        self.rect = pygame.Rect(start_x, y + offset, width, height)

        if direction == DirectionRow.RIGHT:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen) -> None:
        graphics.draw_debug_rect(screen, self.rect, (255, 0, 0))

        screen.blit(self.image, self.rect)

    def update(self, dt, speed) -> None:
        previous_x = self.rect.x

        if self.direction == DirectionRow.LEFT:
            self.pos_x -= speed * dt
        else:
            self.pos_x += speed * dt

        self.rect.x = round(self.pos_x)
        self.delta_x = self.rect.x - previous_x

    def teleport_to(self, x):
        self.pos_x = float(x)
        self.rect.left = round(self.pos_x)

    def reenter(self, zone: pygame.Rect) -> None:
        if self.direction == DirectionRow.LEFT:
            x = zone.right
        else:
            x = zone.left - self.rect.width

        self.teleport_to(x)

    def is_out_of(self, zone: pygame.Rect) -> bool:
        if self.direction == DirectionRow.LEFT:
            return self.rect.right <= zone.left

        return self.rect.left >= zone.right

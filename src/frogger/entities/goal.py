import pygame

from .. import config, graphics


class Goal:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.filled = False

        self.image = graphics.load_image(
            config.DECORS_PATH / "tile_goal.png", self.rect.size
        )
        self.image_filled = graphics.load_image(
            config.FROG_PATH / "grenouille_immobile.png", self.rect.size
        )

    def draw(self, screen):
        graphics.draw_debug_rect(screen, self.rect, (255, 0, 0))

        screen.blit(self.image, self.rect)

        if self.filled:
            screen.blit(self.image_filled, self.rect)

    def fill(self):
        self.filled = True

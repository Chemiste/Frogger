import pygame

from .. import config, graphics
from ..enums.direction import Direction


class Frog:
    def __init__(self, screen_width, screen_height, jump_size):
        self.rect_screen = pygame.Rect(0, 0, screen_width, screen_height)
        self.rect = pygame.Rect(0, 0, config.FROG_HITBOX_SIZE, config.FROG_HITBOX_SIZE)
        self.support = None
        self.reset_position()
        self.jump_size = jump_size
        self.jump_duration_frames = config.FROG_JUMP_ANIMATION_FRAMES
        self.jump_timer = 0

        self._load_images()

    def _load_images(self):
        self.image_static = graphics.load_image(
            config.FROG_PATH / "grenouille_immobile.png",
            (config.FROG_HITBOX_SIZE, config.FROG_HITBOX_SIZE),
        )

        self.image_jump = graphics.load_image(
            config.FROG_PATH / "grenouille_sautant.png",
            (config.FROG_JUMP_DRAW_SIZE, config.FROG_JUMP_DRAW_SIZE),
        )

        self.jump_images = {
            Direction.UP: self.image_jump,
            Direction.LEFT: pygame.transform.rotate(self.image_jump, 90),
            Direction.RIGHT: pygame.transform.rotate(self.image_jump, -90),
            Direction.DOWN: pygame.transform.rotate(self.image_jump, 180),
        }

        self.image_current = self.image_static

    def update(self):
        if self.support is not None:
            self.rect.x += self.support.delta_x

        if self.jump_timer > 0:
            self.jump_timer -= 1
            if self.jump_timer == 0:
                self.image_current = self.image_static

    def move(self, direction):
        self.image_current = self.jump_images[direction]
        self.jump_timer = self.jump_duration_frames

        x = 0
        y = 0

        if direction == Direction.UP:
            y = -self.jump_size
        elif direction == Direction.DOWN:
            y = self.jump_size
        elif direction == Direction.LEFT:
            x = -self.jump_size
        elif direction == Direction.RIGHT:
            x = +self.jump_size

        candidate_rect = self.rect.move(x, y)
        if self.rect_screen.contains(candidate_rect):
            self.rect = candidate_rect

    def draw(self, screen):
        graphics.draw_debug_rect(screen, self.rect, (255, 0, 0))

        image_rect = self.image_current.get_rect(center=self.rect.center)
        screen.blit(self.image_current, image_rect)

    def reset_position(self):
        self.support = None
        self.rect.centerx = self.rect_screen.width / 2
        self.rect.centery = self.rect_screen.height - (config.CELL_SIZE // 2)

    def is_on_screen(self) -> bool:
        return self.rect_screen.contains(self.rect)

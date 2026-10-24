from .. import config
from ..entities.life import Life


class Lives:
    def __init__(self, pos_y):
        self.lives: list[Life] = []

        for i in range(config.TOTAL_LIVES):
            life = Life(
                (i * config.LIFE_ICON_SPACING_PX) + config.LIVES_LEFT_MARGIN_PX,
                pos_y,
            )
            self.lives.append(life)

    def draw(self, screen):
        for life in self.lives:
            life.draw(screen)

    def lose_a_life(self):
        self.lives.pop()

    def has_lives_left(self) -> bool:
        return len(self.lives) > 0

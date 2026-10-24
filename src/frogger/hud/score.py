import pygame

from .. import config


class Score:
    def __init__(self):
        self._jump_score = 0
        self._seconds_score = 0
        self._frog_saved_score = 0

    def jump_forward(self):
        self._jump_score += config.PTS_FORWARD_JUMP

    def left_seconds(self, seconds):
        self._seconds_score += config.PTS_LEFT_SECONDS * seconds

    def frog_saved(self, number, total_possible):
        self._frog_saved_score = number * config.PTS_SAVED_FROG

        if number == total_possible:
            self._frog_saved_score = config.PTS_ALL_SAVED_FROG

    def total_score(self):
        return self._jump_score + self._seconds_score + self._frog_saved_score

    def draw(
        self, screen: pygame.Surface, display_font: pygame.font.Font
    ):
        text_score = f"Score: {self.total_score()}"
        text_surface = display_font.render(text_score, True, "white")
        text_rect = text_surface.get_rect(
            topright=(
                screen.get_width() - config.RIGHT_MARGIN_SCORES_PX,
                config.TOP_MARGIN_SCORES_PX,
            )
        )
        screen.blit(text_surface, text_rect)

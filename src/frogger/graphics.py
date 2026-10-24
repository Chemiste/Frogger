import pygame

from . import config


def load_image(path, size) -> pygame.Surface:
    """Charge une image et la redimensionne à la taille demandée."""
    image = pygame.image.load(path)
    image = pygame.transform.smoothscale(image, size)

    return image


def draw_debug_rect(screen, rect, color):
    """Permet d'afficher un cadre autour de certains objets pour faciliter le debug"""
    if config.DEBUG:
        pygame.draw.rect(screen, color, rect)


def load_image_with_width(path, width) -> pygame.Surface:
    """Charge une image et la redimensionne à une largeur donnée,
    en gardant ses proportions."""
    image = pygame.image.load(path)
    height = round(width * image.get_height() / image.get_width())

    return pygame.transform.smoothscale(image, (width, height))

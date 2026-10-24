from .. import config, graphics


class Life:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = graphics.load_image(
            config.FROG_PATH / "grenouille_immobile.png",
            (config.LIFE_ICON_SIZE_PX, config.LIFE_ICON_SIZE_PX),
        )

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

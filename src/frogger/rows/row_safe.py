from .row import Row


class RowSafe(Row):
    def __init__(self, pos_y, width, height):
        super().__init__(pos_y, width, height, "tile_trottoir.png")

import random

from .. import config, graphics
from ..entities.vehicle import Vehicle
from ..enums.direction_row import DirectionRow
from .row import Row


class RowRoad(Row):
    def __init__(
        self,
        pos_y: int,
        width: int,
        height: int,
        direction: DirectionRow,
        image: str,
        length_cells: int
    ):
        super().__init__(pos_y, width, height, "tile_route.png")

        self.vehicles: list[Vehicle] = []
        self.speed = random.randrange(
            config.VEHICLE_MINIMUM_SPEED,
            config.VEHICLE_MAXIMUM_SPEED + config.VEHICLE_STEP_SPEED,
            config.VEHICLE_STEP_SPEED,
        )

        self.line_image = graphics.load_image(
            config.DECORS_PATH / "tile_ligne_route.png",
            (config.CELL_SIZE, config.CELL_SIZE),
        )

        self._spawn_vehicles(width, direction, image, length_cells)

    def _spawn_vehicles(self, width, direction, image: str, length_cells: int):
        zone_width = round(width / config.NUMBER_OF_VEHICLES_PER_ROW)

        for i in range(config.NUMBER_OF_VEHICLES_PER_ROW):
            start_zone = i * zone_width
            end_zone = (i + 1) * zone_width - (config.CELL_SIZE * length_cells)

            pos_in_zone = random.randrange(start_zone, end_zone, 1)

            self.vehicles.append(
                Vehicle(
                    start_x=pos_in_zone,
                    y=self.rect.y,
                    direction=direction,
                    image=image,
                    vehicle_length=length_cells,
                )
            )

    def _draw_lane_line(self, screen):
        y = self.rect.bottom - (self.line_image.get_height() // 2)

        for col in range(config.COLS):
            screen.blit(self.line_image, (col * config.CELL_SIZE, y))

    def draw_objects(self, screen):
        for vehicle in self.vehicles:
            vehicle.draw(screen)

    def update(self, dt):
        for vehicle in self.vehicles:
            vehicle.update(dt, self.speed)

            if vehicle.is_out_of(self.rect):
                vehicle.reenter(self.rect)

    def is_deadly_for(self, frog) -> bool:
        return any(frog.rect.colliderect(vehicle.rect) for vehicle in self.vehicles)

    def draw_background(self, screen):
        super().draw_background(screen)

        self._draw_lane_line(screen)

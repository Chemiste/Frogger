import random

from .. import config
from ..entities.water_transport import WaterTransport
from ..enums.direction_row import DirectionRow
from .row import Row


class RowRiver(Row):
    def __init__(
        self,
        pos_y,
        width,
        height,
        direction: DirectionRow,
        image: str,
        length_cells: int,
    ):
        super().__init__(pos_y, width, height, "tile_eau.png")

        self.vehicles: list[WaterTransport] = []
        self.speed = random.randrange(
            config.VEHICLE_MINIMUM_SPEED,
            config.VEHICLE_MAXIMUM_SPEED + config.VEHICLE_STEP_SPEED,
            config.VEHICLE_STEP_SPEED,
        )

        self._spawn_vehicles(
            width, direction=direction, image=image, length_cells=length_cells
        )

    def _spawn_vehicles(self, width, direction, image: str, length_cells: int):
        zone_width = round(width / config.NUMBER_OF_VEHICLES_PER_ROW)

        for i in range(config.NUMBER_OF_VEHICLES_PER_ROW):
            start_zone = i * zone_width
            end_zone = (i + 1) * zone_width - (config.CELL_SIZE * 3)

            pos_in_zone = random.randrange(start_zone, end_zone, 1)

            self.vehicles.append(
                WaterTransport(
                    start_x=pos_in_zone,
                    y=self.rect.y,
                    direction=direction,
                    image=image,
                    vehicle_length=length_cells,
                )
            )

    def draw_objects(self, screen):
        for vehicle in self.vehicles:
            vehicle.draw(screen)

    def update(self, dt):
        for vehicle in self.vehicles:

            vehicle.update(dt, self.speed)

            if vehicle.is_out_of(self.rect):
                vehicle.reenter(self.rect)

    def find_support(self, frog) -> WaterTransport | None:
        for vehicle in self.vehicles:
            if frog.rect.colliderect(vehicle.rect):
                return vehicle

        return None

    def is_deadly_for(self, frog) -> bool:
        return frog.rect.colliderect(self.rect) and self.find_support(frog) is None

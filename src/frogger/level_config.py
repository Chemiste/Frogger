from dataclasses import dataclass

from .enums.direction_row import DirectionRow
from .enums.row_type import RowType


@dataclass(frozen=True)
class RowConfig:
    row_type: RowType
    direction: DirectionRow | None = None
    image: str | None = None
    length_cells: int | None = None


GAME_ROW_CONFIGS = [
    RowConfig(RowType.SAFE),
    RowConfig(RowType.ROAD, DirectionRow.LEFT, "voiture_rouge.png", 2),
    RowConfig(RowType.ROAD, DirectionRow.RIGHT, "voiture_orange.png", 2),
    RowConfig(RowType.ROAD, DirectionRow.LEFT, "voiture_vert.png", 2),
    RowConfig(RowType.ROAD, DirectionRow.RIGHT, "camion_bleu.png", 3),
    RowConfig(RowType.ROAD, DirectionRow.LEFT, "camion_orange.png", 3),
    RowConfig(RowType.SAFE),
    RowConfig(RowType.RIVER, DirectionRow.LEFT, "tortues_3.png", 3),
    RowConfig(RowType.RIVER, DirectionRow.RIGHT, "tortues_2.png", 2),
    RowConfig(RowType.RIVER, DirectionRow.LEFT, "tronc_long.png", 3),
    RowConfig(RowType.RIVER, DirectionRow.RIGHT, "tronc_moyen.png", 2),
    RowConfig(RowType.RIVER, DirectionRow.LEFT, "tortues_3.png", 3),
    RowConfig(RowType.GOAL),
]

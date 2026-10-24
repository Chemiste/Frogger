from dataclasses import dataclass

from .. import config
from ..entities.goal import Goal
from ..enums.hit_result import HitResult
from .row import Row


@dataclass
class CollisionStatus:
    hit_result: HitResult
    goal: Goal | None


class RowGoal(Row):
    def __init__(self, pos_y, width, height):
        super().__init__(pos_y, width, height, "tile_espace.png")
        self.goals: list[Goal] = []

        margin = self._compute_margin()
        self._create_goals(margin, pos_y, height)

    def _compute_margin(self) -> int:
        total_size_of_goals = config.NUMBER_OF_GOALS * config.GOAL_WIDTH_CELLS
        total_size_of_space = (config.NUMBER_OF_GOALS - 1) * config.GOAL_GAP_CELLS
        margin_total_cells = config.COLS - total_size_of_goals - total_size_of_space
        margin = margin_total_cells // 2
        return margin

    def _create_goals(self, margin, pos_y, height):
        for i in range(config.NUMBER_OF_GOALS):
            col = margin + i * (config.GOAL_WIDTH_CELLS + config.GOAL_GAP_CELLS)

            goal = Goal(
                col * config.CELL_SIZE,
                pos_y,
                config.GOAL_WIDTH_CELLS * config.CELL_SIZE,
                height,
            )
            self.goals.append(goal)

    def draw_objects(self, screen):
        for goal in self.goals:
            goal.draw(screen)

    def _find_colliding_goal(self, frog) -> Goal | None:
        for goal in self.goals:
            if frog.rect.colliderect(goal.rect):
                # The frog is in a Goal Box
                return goal

        return None

    def check_collision(self, frog) -> CollisionStatus:
        collision_status: CollisionStatus = CollisionStatus(
            hit_result=HitResult.NONE, goal=None
        )

        if frog.rect.colliderect(self.rect):
            # The frog is in the goal row

            collision_status.goal = self._find_colliding_goal(frog)

            if collision_status.goal is None:
                # The frog is not in a goal box but in the row goal,
                # so not in a right place, consider colliding
                collision_status.hit_result = HitResult.DIED
            elif collision_status.goal.filled:
                # The frog is in a goal box but already filled, so colliding
                collision_status.hit_result = HitResult.DIED
            else:
                collision_status.hit_result = HitResult.SUCCESS

        return collision_status

    def count_filled_goals(self) -> int:
        return sum(goal.filled for goal in self.goals)

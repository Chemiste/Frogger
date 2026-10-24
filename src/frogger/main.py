import pygame

from . import config, level_config
from .entities.frog import Frog
from .enums.direction import Direction
from .enums.hit_result import HitResult
from .enums.row_type import RowType
from .hud.lives import Lives
from .hud.score import Score
from .rows.row_goal import RowGoal
from .rows.row_river import RowRiver
from .rows.row_road import RowRoad
from .rows.row_safe import RowSafe


def get_direction(event) -> Direction | None:
    direction = None

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            direction = Direction.UP
        elif event.key == pygame.K_DOWN:
            direction = Direction.DOWN
        elif event.key == pygame.K_LEFT:
            direction = Direction.LEFT
        elif event.key == pygame.K_RIGHT:
            direction = Direction.RIGHT

    return direction


def kill_frog(frog, lives):
    frog.reset_position()
    lives.lose_a_life()


def main():
    pygame.init()
    pygame.font.init()
    display_font = pygame.font.Font(None, config.FONT_SIZE)

    screen_width = config.COLS * config.CELL_SIZE
    screen_height = config.ROWS * config.CELL_SIZE

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    rows = []
    frog = Frog(
        screen_width=screen_width,
        screen_height=screen_height,
        jump_size=config.CELL_SIZE,
    )

    for row in level_config.GAME_ROW_CONFIGS:
        if row.row_type == RowType.SAFE:
            rows.append(RowSafe(
                width=screen_width,
                pos_y=screen_height - (config.CELL_SIZE * (len(rows) + 1)),
                height=config.CELL_SIZE))
        elif row.row_type == RowType.ROAD:
            if row.direction is not None and row.image is not None and row.length_cells is not None:
                rows.append(RowRoad(
                    pos_y=screen_height - (config.CELL_SIZE * (len(rows) + 1)),
                    width=screen_width,
                    height=config.CELL_SIZE,
                    direction=row.direction,
                    image=row.image,
                    length_cells=row.length_cells

                ))
        elif row.row_type == RowType.RIVER:
            if row.direction is not None and row.image is not None and row.length_cells is not None:
                rows.append(RowRiver(
                    pos_y=screen_height - (config.CELL_SIZE * (len(rows) + 1)),
                    width=screen_width,
                    height=config.CELL_SIZE,
                    direction=row.direction,
                    image=row.image,
                    length_cells=row.length_cells
                ))
        elif row.row_type == RowType.GOAL:
            rows.append(RowGoal(width=screen_width, pos_y=0, height=config.CELL_SIZE))

    lives = Lives(pos_y=screen_height - config.LIVES_DISTANCE_FROM_BOTTOM_PX)
    score = Score()

    while running:
        direction = None

        # le while au dessus boucle 60 fois toutes les secondes,
        # et donc le pygame.event.get() contient tous les évènements
        # durant ce laps de temps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # on doit mettre dans une variable new_direction parce que si dans
            # pygame.event.get() on a 2 events (par exemple fleche haut et souris
            # déplacé), pour le 1er event on va bien récupéré une direction
            # (flèche haut), mais dans la deuxième on ne va rien récupérer et donc
            # get_direction va renvoyer None
            new_direction = get_direction(event)
            if new_direction is not None:
                direction = new_direction

        # TODO display GAMEOVER Message when no more lives left
        if lives.has_lives_left():
            frog.update()

            if direction is not None:
                frog.move(direction)

            if direction == Direction.UP:
                score.jump_forward()

            for row in rows:
                row.update(dt)

            frog.support = None

            for row in rows:
                if row.is_deadly_for(frog):
                    kill_frog(frog, lives)
                    break

                support = row.find_support(frog)
                if support is not None:
                    frog.support = support

            if not frog.is_on_screen():
                kill_frog(frog, lives)

            row_goal = rows[len(rows)-1]
            collision_status =  row_goal.check_collision(frog)

            if collision_status.hit_result == HitResult.DIED:
                kill_frog(frog, lives)
            elif collision_status.hit_result == HitResult.SUCCESS:
                if collision_status.goal is not None:
                    collision_status.goal.fill()
                    score.frog_saved(
                        row_goal.count_filled_goals(), config.NUMBER_OF_GOALS
                    )

                frog.reset_position()

            screen.fill("black")

            for row in rows:
                row.draw_background(screen)

            for row in rows:
                row.draw_objects(screen)

            frog.draw(screen)
            lives.draw(screen)

            score.draw(screen, display_font)

            pygame.display.flip()

            dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()

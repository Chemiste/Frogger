from pathlib import Path

DEBUG = False

# The screen is divided in number of columns
COLS = 23

# How many rows will be displayed in the game
# (Row1 : Starting Row, Row2 : vehicle from right to left...)
ROWS = 13

# Size in pixel of a box, this size will determine the size of the playing surface
# (screenwidth = cols * cell_size, screenheight = rows * cell_size)
CELL_SIZE = 56

ASSETS_PATH = Path(__file__).resolve().parent / "assets"
FROG_PATH = ASSETS_PATH / "frog"
VEHICLE_PATH = ASSETS_PATH / "vehicles"
DECORS_PATH = ASSETS_PATH / "decors"
RIVER_PATH = ASSETS_PATH / "river"

NUMBER_OF_VEHICLES_PER_ROW = 4

# How many cells to draw a goal
GOAL_WIDTH_CELLS = 1

# How many cells between each goal
GOAL_GAP_CELLS = 3

# Number of "target" section at the top of screen
NUMBER_OF_GOALS = 5

# Number of lives for the player
TOTAL_LIVES = 3

# How many points when the frog go forward
PTS_FORWARD_JUMP = 10

# How many points when a frog go into an empty goal
PTS_SAVED_FROG = 50

# How many points when all frogs are saved
PTS_ALL_SAVED_FROG = 1000

# How many points for each seconds left
PTS_LEFT_SECONDS = 10

# Size of the hitbox of the frog
FROG_HITBOX_SIZE = 40

# The size of the image when the frog jumps.
FROG_JUMP_DRAW_SIZE = 80

# Where to put the lives frame from the bottom of the screen
LIVES_DISTANCE_FROM_BOTTOM_PX = 35
# Where to put the lives frame from the left of the screen
LIVES_LEFT_MARGIN_PX = 10

# Size in pixels of each life icon
LIFE_ICON_SIZE_PX = 20

# Size in pixels of space between each life icon
LIFE_ICON_SPACING_PX = 30

TOP_MARGIN_SCORES_PX = 20
RIGHT_MARGIN_SCORES_PX = 20

VEHICLE_MINIMUM_SPEED = 50
VEHICLE_MAXIMUM_SPEED = 150
VEHICLE_STEP_SPEED = 25

FONT_SIZE = 24

FROG_JUMP_ANIMATION_FRAMES = 15

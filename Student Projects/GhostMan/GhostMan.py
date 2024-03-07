import pygame as pg

# Constants
WIDTH, HEIGHT = 800, 700
FPS = 60

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ghost Man")

# Maze layout using a 2D array
maze = [
    "|||||||||||||||||||||||||||",
    "|............|............|",
    "|.||||.|||||.|.|||||.||||.|",
    "|.||||.|||||.|.|||||.||||.|",
    "|.........................|",
    "|.||||.||.|||||||.||.||||.|",
    "|......||....|....||......|",
    "|.||||.||||| | |||||.||||.|",
    "|.||||.||         ||.||||.|",
    "|.||||.||  |||||  ||.||||.|",
    "      .    |EEE|    .      ",
    "|.||||.||  |||||  ||.||||.|",
    "|.||||.||         ||.||||.|",
    "|.||||.||.|||||||.||.||||.|",
    "|............|............|",
    "|.||||.|||||.|.|||||.||||.|",
    "|....|.......P.......|....|",
    "|||..|.||.|||||||.||.|..|||",
    "|......||....|....||......|",
    "|.||||||||||.|.||||||||||.|",
    "|.........................|",
    "|||||||||||||||||||||||||||"
]

# Maze cell size
cell_size = int(WIDTH / 27)

# Pac-Man properties
pacman_size = cell_size / 2
pacman_args = pg.Rect(cell_size, cell_size, pacman_size, pacman_size)
pacman_pos = {"x": 16, "y": 13}
pacman_direction = pg.Vector2(0, 0)

# Function to draw the maze
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pg.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == "|":
                pg.draw.rect(screen, BLUE, rect)
            elif cell == "-":
                pg.draw.rect(screen, BLACK, rect)
            elif cell == ".":
                dot_rect = pg.Rect(rect.centerx - 2, rect.centery - 2, 5, 5)
                pg.draw.rect(screen, WHITE, dot_rect)
            elif cell == "P":
                pacman_args.x = x * cell_size + pacman_size / 2
                pacman_args.y = y * cell_size + pacman_size / 2
                pacman_pos["x"] = y
                pacman_pos["y"] = x
                pg.draw.circle(screen, YELLOW, pacman_args.center, pacman_size)
                
# Function to check if there are any pellets left in the maze
def pellets_left(maze):
    return any('.' in row for row in maze)

# Game loop
running = True
clock = pg.time.Clock()
last_frame = clock.get_time()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # Update Pac-Man position based on direction
    next_y = int(pacman_pos["y"] + pacman_direction.y)
    next_x = int(pacman_pos["x"] + pacman_direction.x)

    # Check for user input to change Pac_Man's direction
    if keys[pg.K_RIGHT]:
        pacman_direction.y = 1
        pacman_direction.x = 0
    elif keys[pg.K_DOWN]:
        pacman_direction.x = 1
        pacman_direction.y = 0
    elif keys[pg.K_LEFT]:
        pacman_direction.y = -1
        pacman_direction.x = 0
    elif keys[pg.K_UP]:
        pacman_direction.x = -1
        pacman_direction.y = 0

    # Keep track of time to control how often the game updates
    last_frame += clock.get_time()

    # Execute the following block only if enough time has passed
    if last_frame >= 150:
        
        # Check if there are pellets left in the maze
        if not pellets_left(maze):
            running = False

        # Check if the next position is within the maze boundaries
        if 0 < next_y < len(maze[pacman_pos["x"]]) and \
        (not (maze[pacman_pos["x"]][next_y] == "|")) and \
        0 < next_x < len(maze) and \
        (not (maze[next_x][pacman_pos["y"]] == "|")):
            
            # Clear Pac-Man's current position in maze
            maze[pacman_pos["x"]] = maze[pacman_pos["x"]][:pacman_pos["y"]] + \
                        " " + maze[pacman_pos["x"]][pacman_pos["y"] + 1:]
            
             # Update Pac-Man's position based on the direction
            pacman_pos["x"] += int(pacman_direction.x)
            pacman_pos["y"] += int(pacman_direction.y)

            # Mark the new position of Pac-Man with "P" in the maze
            maze[pacman_pos["x"]] = maze[pacman_pos["x"]][:pacman_pos["y"]] + \
                    "P" + maze[pacman_pos["x"]][pacman_pos["y"] + 1:]

        # Reset the timer for the next frame    
        last_frame = 0

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Draw the maze
    draw_maze(maze)

    # Draw Pac-Man
    pg.draw.circle(screen, YELLOW, pacman_args.center, pacman_size)

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pg.quit()

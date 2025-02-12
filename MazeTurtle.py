import turtle
import random
import time

# Set up screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver with Random Endpoint")
wn.setup(1366, 768)

# Create maze turtle
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.shape("square")
maze_turtle.shapesize(1.8, 1.8)
maze_turtle.penup()
maze_turtle.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.shape("circle")
player.color("black")
player.shapesize(1.5, 1.5)
player.penup()
player.speed(0)

# Generate a random maze
rows, cols = 15, 21
cell_size = 40
maze = [["X" for _ in range(cols)] for _ in range(rows)]

def generate_random_maze():
    def carve_passages(y, x):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        for _ in range(2):  # Introduce multiple passes for complexity
            random.shuffle(directions)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols - 1 and maze[ny][nx] == "X":
                    if random.random() > 0.3:  # 70% chance to create a turn
                        maze[ny][nx] = " "
                        maze[y + dy // 2][x + dx // 2] = " "
                        carve_passages(ny, nx)

    maze[1][1] = " "  # Starting point
    carve_passages(1, 1)
    
    # Randomly choose an endpoint in any open area
    open_cells = [(y, x) for y in range(1, rows) for x in range(1, cols) if maze[y][x] == " "]
    if open_cells:
        ey, ex = random.choice(open_cells)
        maze[ey][ex] = "E"

# Draw the maze
def draw_maze(maze):
    offset_x = -(cols * cell_size) // 2 + cell_size // 2
    offset_y = (rows * cell_size) // 2 - cell_size // 2

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = offset_x + (x * cell_size)
            screen_y = offset_y - (y * cell_size)
            if maze[y][x] == "X":
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.color("green")
                maze_turtle.stamp()
            elif maze[y][x] == "E":
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.color("red")
                maze_turtle.stamp()

# Function to mark the path with yellow
def mark_path(x, y):
    screen_x = -(cols * cell_size) // 2 + x * cell_size + cell_size // 2
    screen_y = (rows * cell_size) // 2 - y * cell_size - cell_size // 2
    maze_turtle.goto(screen_x, screen_y)
    maze_turtle.color("yellow")
    maze_turtle.stamp()

# Recursive function to solve the maze
def solve_maze(x, y):
    if maze[y][x] == "X" or maze[y][x] == "2":  # Wall or already visited
        return False

    # Check if this cell is the end point
    if maze[y][x] == "E":
        player.goto(-cols * cell_size // 2 + x * cell_size + cell_size // 2, rows * cell_size // 2 - y * cell_size - cell_size // 2)
        print("Maze solved! Exiting the game...")
        time.sleep(2)
        wn.bye()
        return True

    maze[y][x] = "2"  # Mark the cell as visited
    mark_path(x, y)
    player.goto(-cols * cell_size // 2 + x * cell_size + cell_size // 2, rows * cell_size // 2 - y * cell_size - cell_size // 2)
    wn.update()
    time.sleep(0.05)

    # Recursively explore neighboring cells in a random order
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dy, dx in directions:
        if solve_maze(x + dx, y + dy):
            return True

    # Backtrack
    player.goto(-cols * cell_size // 2 + x * cell_size + cell_size // 2, rows * cell_size // 2 - y * cell_size - cell_size // 2)
    time.sleep(0.05)
    return False

# Generate the maze
generate_random_maze()

# Set tracer to reduce rendering lag
wn.tracer(0)

# Draw the generated maze
draw_maze(maze)

# Align the player to the starting point (1, 1)
player.goto(-cols * cell_size // 2 + cell_size + cell_size // 2, rows * cell_size // 2 - cell_size - cell_size // 2)

# Solve the maze
solve_maze(1, 1)

# Main loop
wn.mainloop()

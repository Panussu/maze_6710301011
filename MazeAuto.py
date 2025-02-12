import turtle
import time

class Maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
            [" ", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
            ["X", "X", "X", " ", "X", " ", "X", "X", "X", " ", " ", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", "X", " ", "X", "X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        self.start = Pos(14, 1)
        self.end = Pos(6, 0)
        self.visited = set()

        # Turtle setup
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.window = turtle.Screen()
        self.window.setup(800, 800)
        self.window.tracer(0)
        self.cell_size = 40

        self.draw_maze()

    def draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                screen_x = x * self.cell_size - 260
                screen_y = 260 - y * self.cell_size
                if self.maze[y][x] == "X":
                    self.draw_square(screen_x, screen_y, "black")
                elif (y, x) == (self.start.y, self.start.x):
                    self.draw_square(screen_x, screen_y, "blue")  # Start
                elif (y, x) == (self.end.y, self.end.x):
                    self.draw_square(screen_x, screen_y, "green")  # End
        self.window.update()

    def draw_square(self, x, y, color):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.fillcolor(color)
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(self.cell_size)
            self.turtle.right(90)
        self.turtle.end_fill()

    def solve(self):
        print("Starting position:", self.start.y, self.start.x)
        print("Ending position:", self.end.y, self.end.x)
        path = self.find_path(self.start.y, self.start.x)
        if path:
            print("\n>>>>> Maze Solved <<<<<\n")
        else:
            print("No solution found.")
        self.window.mainloop()

    def find_path(self, y, x):
        if not self.is_in_bound(y, x) or (y, x) in self.visited or not self.is_walkable(y, x):
            return None

        if (y, x) == (self.end.y, self.end.x):
            self.mark_cell(y, x, "green")
            time.sleep(0.1)
            return [(y, x)]

        self.visited.add((y, x))
        self.mark_cell(y, x, "yellow")
        time.sleep(0.1)

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            path = self.find_path(y + dy, x + dx)
            if path:
                return [(y, x)] + path

        self.mark_cell(y, x, "red")
        time.sleep(0.1)
        return None

    def mark_cell(self, y, x, color):
        screen_x = x * self.cell_size - 260
        screen_y = 260 - y * self.cell_size
        self.draw_square(screen_x, screen_y, color)
        self.window.update()

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def is_walkable(self, y, x):
        return self.maze[y][x] in (" ", "E")


class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x


if __name__ == "__main__":
    m = Maze()
    m.solve()

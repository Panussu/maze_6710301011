import os
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", " ", " ", "X"],
            ["X", "X", "X", " ", "X", " ", "E"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", " ", " ", "X", "X", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", "S", "X", "X", "X", "X", "X"],
        ]
        self.start = pos(6, 1)  # Starting position (row 6, column 1)
        self.current = pos(6, 1)  # Current player position
        self.end = pos(2, 6)   # Ending position (row 2, column 6)

    def isInBound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def isWalkable(self, y, x):
        return self.maze[y][x] in (" ", "E")

    def print(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def move(self, direction):
        dy, dx = 0, 0
        if direction == 'w':  # Up
            dy, dx = -1, 0
        elif direction == 's':  # Down
            dy, dx = 1, 0
        elif direction == 'a':  # Left
            dy, dx = 0, -1
        elif direction == 'd':  # Right
            dy, dx = 0, 1

        new_y, new_x = self.current.y + dy, self.current.x + dx

        if self.isInBound(new_y, new_x) and self.isWalkable(new_y, new_x):
            # Update player position
            self.maze[self.current.y][self.current.x] = " "  # Clear current position
            self.current.y, self.current.x = new_y, new_x
            if self.maze[new_y][new_x] == "E":
                self.maze[new_y][new_x] = "P"
                self.print()
                print("\n>>>>> Maze Solved <<<<<\n")
                return False
            self.maze[new_y][new_x] = "P"  # Mark new position
        else:
            print("Invalid move. Try again.")

        return True

class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':
    m = maze()
    m.maze[m.start.y][m.start.x] = "P"
    m.maze[m.end.y][m.end.x] = "E"
    m.print()

    while True:
        direction = input("Enter your move (w/a/s/d): ").strip().lower()
        if direction in ('w', 'a', 's', 'd'):
            if not m.move(direction):
                break
            m.print()
        else:
            print("Invalid input. Please use 'w', 'a', 's', 'd' to move.")

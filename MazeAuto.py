import os
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", " ", " ", "X"],
            ["X", "X", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", " ", " ", "X", "X", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.start = pos(6, 1)  # Starting position (row 6, column 1)
        self.end = pos(2, 6)   # Ending position (row 2, column 6)
        self.visited = set()

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

    def solve(self):
        print("Starting position:", self.start.y, self.start.x)
        print("Ending position:", self.end.y, self.end.x)
        path = self.find_path(self.start.y, self.start.x)
        if path:
            for step in path:
                self.maze[step[0]][step[1]] = "P"
                self.print()
                time.sleep(0.25)
            print("\n>>>>> Maze Solved <<<<<\n")
        else:
            print("No solution found. Debugging info:")
            self.debug_print_visited()

    def find_path(self, y, x):
        # Base case: check if position is valid, visited, or walkable
        if not self.isInBound(y, x) or (y, x) in self.visited or not self.isWalkable(y, x):
            return None

        # Check if we have reached the end position
        if (y, x) == (self.end.y, self.end.x):
            return [(y, x)]

        # Mark the current position as visited
        self.visited.add((y, x))
        self.maze[y][x] = "I"  # Mark as visited in the maze
        self.print()
        time.sleep(0.1)

        # Explore neighbors using backtracking: down, right, up, left
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_y, next_x = y + dy, x + dx
            path = self.find_path(next_y, next_x)
            if path:
                return [(y, x)] + path  # Add current position to the successful path

        # Backtrack: Mark as a dead-end
        self.maze[y][x] = "O"
        self.print()
        time.sleep(0.1)
        return None

    def debug_print_visited(self):
        print("Visited positions:")
        for y, x in sorted(self.visited):
            print(f"({y}, {x})")

        print("\nMaze with visited positions:")
        for row in self.maze:
            print(" ".join(row))

class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':
    m = maze()
    m.print()
    m.solve()

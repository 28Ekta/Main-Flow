# Task:  Maze Generator and Solver (DFS Based, Text Visualization)
import random
import sys

# Increase recursion depth for larger mazes
sys.setrecursionlimit(10000)

# Maze dimensions (must be odd numbers)
WIDTH = 21
HEIGHT = 21

# Cell values
WALL = 1
PATH = 0
VISITED = 2
SOLUTION = 3

# Directions to move (jump over walls)
DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def generate_maze(width, height):
    # Create a full wall grid
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        maze[y][x] = PATH
        random.shuffle(DIRS)
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == WALL:
                    # Carve the wall between
                    maze[y + dy//2][x + dx//2] = PATH
                    carve(nx, ny)

    carve(1, 1)
    return maze

def print_maze(maze, start, end):
    symbols = {
        WALL: "█",     # solid block for walls
        PATH: " ",     # space for path
        VISITED: "·",  # visited dead-ends
        SOLUTION: "•"  # dots for solution path
    }
    top_bottom = "╔" + ("═" * len(maze[0])) + "╗"
    print(top_bottom)
    for y, row in enumerate(maze):
        line = "║"
        for x, cell in enumerate(row):
            if (y, x) == start:
                line += "S"
            elif (y, x) == end:
                line += "E"
            else:
                line += symbols.get(cell, "?")
        line += "║"
        print(line)
    print("╚" + ("═" * len(maze[0])) + "╝")

def solve_maze(maze, x, y, end):
    if (y, x) == end:
        return True

    if maze[y][x] != PATH:
        return False

    maze[y][x] = SOLUTION

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if solve_maze(maze, nx, ny, end):
            return True

    maze[y][x] = VISITED
    return False

def main():
    maze = generate_maze(WIDTH, HEIGHT)
    start = (1, 1)
    end = (HEIGHT - 2, WIDTH - 2)

    print("\nGenerated Maze:\n")
    print_maze(maze, start, end)

    if solve_maze(maze, start[1], start[0], end):
        print("\nSolved Maze:\n")
        print_maze(maze, start, end)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()

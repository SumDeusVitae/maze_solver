from graphics import Window, Line, Point
from cell import Cell

from maze import Maze
import sys



def main():
    sys.setrecursionlimit(1000)
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    solved = maze.solve()
    if solved:
        print("Maze solved")
    else:
        print("Maze can't be solved")


    
    win.wait_for_close()

if __name__ == "__main__":
    main()
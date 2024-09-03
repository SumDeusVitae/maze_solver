from graphics import Window, Line, Point, Cell



def main():
    win = Window(800,600)
    cell1 = Cell(50, 50, 75, 75, win)
    cell2 = Cell(100, 100, 150, 150, win)

    
    # Draw the cell
    cell1.draw()
    cell2.has_left_wall = False
    cell2.draw()

    
    win.wait_for_close()

if __name__ == "__main__":
    main()
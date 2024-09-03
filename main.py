from graphics import Window, Line, Point, Cell



def main():
    win = Window(800,600)
    cell1 = Cell(50, 50, 75, 75, win)
    cell2 = Cell(75, 50, 100, 75, win)
    cell3 = Cell(50, 100, 75, 125, win)
    cell4 = Cell(75, 100, 100, 125, win)

    
    # Draw the cell
    cell1.has_right_wall = False
    cell1.draw()
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw()
    cell1.draw_move(cell2)

    cell3.has_right_wall = False
    cell3.draw()
    cell4.has_left_wall = False
    cell4.draw()
    cell3.draw_move(cell4, True)


    
    win.wait_for_close()

if __name__ == "__main__":
    main()
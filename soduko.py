from cell import Cell
from window import Window,Point,Line
import time
from tkinter import *
import random
import numpy as np

class Soduko():

    def __init__(self,window,difficulty = "Normal"):
        self._window = window
        self._difficulty = difficulty
        self._vertical_cells = 9
        self._horizontel_cells = 9
        self._cells = np.empty((self._vertical_cells,self._horizontel_cells),dtype=object)
        self._x = 20 
        self._y = 20
        self._cell_size = 40

    def _create_cells(self):
        for x in range(self._horizontel_cells):
            for y in range(0,self._vertical_cells):
                self._cells[x,y]= Cell(self._window,x_cords = x,y_cords = y)


    def _draw_walls(self):
        x0 = self._x
        x1 = self._x + (3 * self._cell_size)
        x2 = self._x + (6 * self._cell_size)
        x3 = self._x + (9 * self._cell_size)
        y0 = self._y
        y1 = self._y + (3 * self._cell_size)
        y2 = self._y + (6 * self._cell_size)
        y3 = self._y + (9 * self._cell_size)

        line1 = Line(Point(x1,y0),Point(x1,y3))
        self._window.draw_line(line1,"red")
        line2 = Line(Point(x2,y0),Point(x2,y3))
        self._window.draw_line(line2,"red") 
        line3 = Line(Point(x0,y1),Point(x3,y1))
        self._window.draw_line(line3,"red") 
        line4 = Line(Point(x0,y2),Point(x3,y2))
        self._window.draw_line(line4,"red") 

    def _draw_cell(self,x,y):
        if self._window is None:
            return
        
        cell_x1 = self._x + (x * self._cell_size)
        cell_x2 = self._x + ((x+1) * self._cell_size)
        cell_y1 = self._y+ (y * self._cell_size)
        cell_y2 = self._y + ((y + 1) * self._cell_size)

        self._cells[x,y].draw(cell_x1,cell_y1,cell_x2,cell_y2)
    

    def _animate(self):
        self._window.redraw()
        time.sleep(1)

    def _valid_placement(self,x,y,number):
        x1_group = 3 * (x//3)
        x2_group = 3 * ((x//3)+1)
        y1_group = 3 * (y//3)
        y2_group = 3 * ((y//3)+1)

        y_line = self._cells[:, y].tolist()
        x_line = self._cells[x, :].tolist()
        group = self._cells[x1_group:x2_group, y1_group:y2_group].flatten().tolist()
        combined_set = set(x_line + y_line + group)
        values_set = {obj.number for obj in combined_set}
        
        if number in values_set:
            return False
        else:
            return True
        
    def _find_open(self):
        for x in range(0,self._horizontel_cells):
            for y in range(0,self._vertical_cells):
                if self._cells[x,y].number == 0:
                    
                    return (x,y)
        else:
            return None

    def _solve_r(self):
        find = self._find_open()
        if not find:
            return True
        else:
            x,y = find
        for i in range(0,10):
            if self._valid_placement(x,y,i):
                self._cells[x,y].number = i
                print(self._cells[x,y].number)
                if self._solve_r():
                    return True
                self._cells[x,y].number = 0 
        return False
        
        

    def _seeding(self):
        
        numbers = [1,2,3,4,5,6,7,8,9]
        random.shuffle(numbers)
        for x in range(0,9,3):
            for y in range (0,9,3):                  
                x1_group = 3 * (x//3)
                x2_group = 3 * ((x//3)+1)
                y1_group = 3 * (y//3)
                y2_group = 3 * ((y//3)+1)   

                group = self._cells[x1_group:x2_group,y1_group:y2_group]
                subchoice = random.choice(group)
                choice = random.choice(subchoice)
                choice.number = numbers[0]
                numbers = numbers[1:]
                
    def _draw_soduko(self):
        for x in range(0,self._horizontel_cells):
            for y in range(0,self._vertical_cells):
                self._draw_cell(x,y)
                self._window.create_label(self._x,self._y,x,y,self._cell_size,self._cells[x,y].number)
                self._draw_walls()

    

    
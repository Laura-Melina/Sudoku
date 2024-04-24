from window import Point,Line,Window
from tkinter import*

class Cell():
    def __init__(self,window,x_cords,y_cords,wrong = False):
        self._win = window
        self.number = 0
        self.x_cords = x_cords
        self.y_cords = y_cords
        self.wrong = wrong
    
    def __repr__(self):
        return f"Cell({self.number},{self.wrong})"
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        
        line_left = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
        self._win.draw_line(line_left)
        
        line_right = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
        self._win.draw_line(line_right)
   
        line_top = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
        self._win.draw_line(line_top)
          
        line_bottom = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
        self._win.draw_line(line_bottom)
   
           
    
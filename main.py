from tkinter import Entry
from window import Window
from soduko import Soduko
def main():

    window = Window(800,600)

    soduko = Soduko(window)
    soduko._create_cells()
    soduko._seeding()
    soduko._solve_r()
    soduko._draw_soduko()
    window.wait_for_close()
main()
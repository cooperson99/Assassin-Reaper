import tkinter

import random

ROWS = 25
COLS = 25
TILE_SIZE = 25
class Tile:
    def __init__(self, x, y):
        self.x = y
        self.x = x
        self.y = y

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

window = tkinter.Tk()
window.title("Snak")
window.resizable(False, False)
canvas = tkinter.Canvas(window, background="black", borderwidth=0, highlightthickness=0, width=WINDOW_WIDTH, height= WINDOW_HEIGHT)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_height/2))
window_y = int((screen_width/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
def draw():
    global snake

    canvas.create_rectangle(snake.x, snake.y, snake.x +TILE_SIZE, snake.y+ TILE_SIZE, fill = "lime green")
    canvas.create_rectangle(food.x, food.y, food.x + food.x)
    window.after(100, draw)

draw()


window.mainloop()
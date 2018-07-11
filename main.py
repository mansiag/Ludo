import tkinter as tk
from settings import *
from board import *
from coin import *

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}'.format(width, height))
root.title('Ludo')

ludo = LudoBoard(root)
ludo.create()
green = Coin(ludo.getcanvas(), 60, 60, color='green')

root.mainloop()
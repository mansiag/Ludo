import tkinter as tk
from settings import *
from board import *
from coin import *
import time

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}'.format(width, height))
root.title('Ludo')

ludo = LudoBoard(root)
ludo.create()
green = []
red = []
yellow = []
blue = []
test = Coin(ludo.get_canvas(), 80, 80, color='green')
green.append(test)




root.mainloop()
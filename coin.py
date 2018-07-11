import tkinter as tk
import os
from PIL import ImageTk, Image
from settings import *

class Coin:

	def __init__(self, master, x, y, color):
		self.canvas = master
		self.curr_x = x
		self.curr_y = y
		self.home_x = x
		self.home_y = y
		self.color = color
		coin = ImageTk.PhotoImage(Image.open(os.getcwd() + "/assets/" + color + ".gif"))
		self.img =  self.canvas.create_image(x + Board.SQUARE_SIZE/2, y + Board.SQUARE_SIZE/2, image=coin)


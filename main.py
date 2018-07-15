import tkinter as tk
from time import sleep
from random import choice

from settings import *
from board import *
from PIL import ImageTk, Image


class Coin:

    def __init__(self, master, x, y, color, coin_index, path_list, flag):
        self.canvas = master
        self.curr_x = x
        self.curr_y = y
        self.home_x = x
        self.home_y = y
        self.color = color
        self.coin_index = coin_index
        self.curr_index = -1
        self.coin = ImageTk.PhotoImage(Image.open('./assets/' + color + '.gif'))
        self.img =  self.canvas.create_image(x, y, anchor=tk.NW, image=self.coin)
        self.canvas.tag_bind(self.img, '<1>', self.onClick)
        self.disable = True
        self.path_list = path_list
        self.flag = flag

    def onClick(self, event):

        if self.disable:
            return

        count = 0
        for goti in colors[self.flag]:
            if goti.is_at_home():
                count += 1

        roll = Dice.roll
        if (count == 4) and (6 not in roll):
            Dice.set(self.flag) 
            roll = []
            Dice.roll = []

        if self.is_at_home():
            if 6 in roll:
                self.canvas.coords(self.img, self.path_list[0][0] + 2, self.path_list[0][1] + 2)
                self.curr_x = self.path_list[0][0]
                self.curr_y = self.path_list[0][1]
                self.curr_index = 0
                Dice.remove_by_index(6)
        else:
            for i in range(roll[0]):
                self.curr_index += 1
                self.canvas.coords(self.img, self.path_list[self.curr_index][0] + 2, self.path_list[self.curr_index][1] + 2)
                self.curr_x = self.path_list[self.curr_index][0]
                self.curr_y = self.path_list[self.curr_index][1]
                self.canvas.update()
                sleep(0.05)
            Dice.remove()
        
        if len(Dice.roll) == 0:
            Dice.set(self.flag)

            next_label = tk.Label(ludo.get_frame(), text=self.get_next_label_text(), font=(None, 20), width=30, height=3,
                                    borderwidth=3, relief=tk.SUNKEN)
            next_label.place(x=100, y=100)
            roll_label = tk.Label(ludo.get_frame(), text='ROLL PLEASE', font=(None, 20), width=30, height=3, borderwidth=3, relief=tk.RAISED)
            roll_label.place(x=100, y=200)



    def change_state(self, flag):
        if flag == self.flag:
            self.disable = False
        else:
            self.disable = True

    def is_at_home(self):
        if self.curr_x == self.home_x and self.curr_y == self.home_y:
            return True
        else:
            return False

    def get_next_label_text(self):
        return '{} turn over, Now {} turn'.format(self.color.title(), turn[self.flag])


class Dice:

    roll = []
    
    @classmethod
    def rolling(cls):
        temp = choice(range(1, 8))
        if temp > 6:
            temp = 6

        if len(cls.roll) == 0 :
            cls.roll.append(temp)
                   
        elif cls.roll[-1] == 6 :
            cls.roll.append(temp)

        if cls.roll.count(6) == 3:
            cls.roll = []

        roll_label = tk.Label(ludo.get_frame(), text='{}'.format(' | '.join([str(x) for x in cls.roll])),
                                 font=(None, 20), width=30, height=3, borderwidth=3, relief=tk.RAISED)
        roll_label.place(x=100, y=200)

    @classmethod
    def set(cls, flag):
        flag += 1
        if flag == 4:
            flag = 0 

        for i in range(4):
            for j in range(4):
                colors[i][j].change_state(flag)

    @classmethod
    def remove(cls):
        Dice.roll.pop(0)

    @classmethod
    def remove_by_index(cls, ex):
        del cls.roll[cls.roll.index(ex)]


def align(x, y, color, path_list, flag):
    container = []
    for i in range(2):
        test = Coin(ludo.get_canvas(), x, y + i*2*Board.SQUARE_SIZE, color=color, coin_index=i, path_list=path_list, flag=flag)
        container.append(test)
    for i in range(2):
        test = Coin(ludo.get_canvas(), x + 2*Board.SQUARE_SIZE, y + i*2*Board.SQUARE_SIZE, color=color, coin_index=i+2, path_list=path_list, flag=flag)
        container.append(test)
    return container




root = tk.Tk()
flag = 0
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}'.format(width, height))
root.title('Ludo')

ludo = LudoBoard(root)
ludo.create()

start_label = tk.Label(ludo.get_frame(), text='! START ! Let\'s Begin with Green.', font=(None, 20),
                         width=30, height=3, borderwidth=3, relief=tk.SUNKEN)
start_label.place(x=100, y=100)

turn = ['Red', 'Blue', 'Yellow', 'Green']

colors = []
colors.append(align(2*Board.SQUARE_SIZE, 2*Board.SQUARE_SIZE, color='green', path_list=path.green_path, flag=0))
colors.append(align(2*Board.SQUARE_SIZE, 11*Board.SQUARE_SIZE, color='red', path_list=path.red_path, flag=1))
colors.append(align(11*Board.SQUARE_SIZE, 11*Board.SQUARE_SIZE, color='blue', path_list=path.blue_path, flag=2))
colors.append(align(11*Board.SQUARE_SIZE, 2*Board.SQUARE_SIZE, color='yellow', path_list=path.yellow_path, flag=3))

button = tk.Button(ludo.get_frame(), text='ROLL', command=Dice.rolling, width=20, height=2)
button.place(x=220, y=470)


for i in range(4):
    for j in range(4):
        colors[i][j].change_state(0)

root.mainloop()

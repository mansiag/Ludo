class Color:

    GREEN = '#0CED2C'
    RED = '#F71313'
    YELLOW = '#FFFF00'
    BLUE = '#3575EC'
    DEFAULT = '#E9E9E9'
    CYAN = '#4EB1BA'


class Board:

    SQUARE_SIZE = 40
    PANEL_WIDTH = 600
    PANEL_HEIGHT = 640
    BOARD_WIDTH = 640
    BOARD_HEIGHT = 640
    POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]
    POSITIVE_V = [(6, 2), (8, 1), (6, 13), (8, 12)]
    POSITIVE_H = [(1, 6), (2, 8), (13, 8), (12, 6)]



class Text:

    MADE_BY = 'Made By: Mansi Agrawal & Shivam Gupta'
    HEADER =  'LUDO - THE GAME'


class Path:

    def __init__(self):

        self.Green_Path = []
        self.Red_Path = []
        self.Blue_Path = []
        self.Yellow_Path = []
        #1
        gx = 60
        gy = 20
        ry = 540
        by = 340
        for i in range(5):
            if i == 0:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx  +  i*40, gy, p))
            self.Red_Path.append((gy, ry  -  i*40, p))
            self.Blue_Path.append((ry - i*40, by, p))
            self.Yellow_Path.append((by, gx - i*40, p))

        #2
        gx = 260
        gy = 220
        ry = 340
        by = 380
        for i in range(5):
            if i == 3:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx, gy - i*40, p))
            self.Red_Path.append((gy - i*40,ry, p))
            self.Blue_Path.append((ry, by - i*40, p))
            self.Yellow_Path.append((by + i*40, gx, p))

        #3
        gx = 260
        gy = 20
        ry = 340
        by = 580
        for i in range(3):
            self.Green_Path.append((gx + i*40, gy, 0))
            self.Red_Path.append((gy, ry - i*40, 0))
            self.Blue_Path.append((ry - i*40, by, 0))
            self.Yellow_Path.append((by, gx + i*40, 0))

        #4
        gx = 340
        gy = 60
        ry = 260
        by = 540
        for i in range(5):
             if i == 0:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx, gy + i*40, p))
            self.Red_Path.append((gy + i*40, ry, p))
            self.Blue_Path.append((ry, by - i*40, p))
            self.Yellow_Path.append((by - i*40, gx, p))

        #5
        gx = 380
        gy = 260
        ry = 220
        by = 340  
        for i in range(5):
            if i == 3:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx + i*40, gy, p))
            self.Red_Path.append((gy, ry - i*40, p))
            self.Blue_Path.append((ry - i*40, by, p))
            self.Yellow_Path.append((by, gx + i*40, p))

        #6
        gx = 580
        gy = 260
        ry = 20
        by = 340
        for i in range(3):
            self.Green_Path.append((gx, gy + i*40, 0))
            self.Red_Path.append((gy + i*40,ry, 0))
            self.Blue_Path.append((ry, by - i*40, 0))
            self.Yellow_Path.append((by - i*40, gx, 0))

        #7
        gx = 540
        gy = 340
        ry = 60
        by = 260
        for i in range(5):
            if i == 0:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx - i*40, gy, p))
            self.Red_Path.append((gy, ry + i*40, p))
            self.Blue_Path.append((ry - i*4, by, p))
            self.Yellow_Path.append((by, gx + i*40, p))

        #8
        gx = 360
        gy = 380
        ry = 260
        by = 220
        for i in range(5):
            if i == 3:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx, gy + i*40, p))
            self.Red_Path.append((gy + i*40, ry,p))
            self.Blue_Path.append((ry, by - i*40, p))
            self.Yellow_Path.append((by - i*40, gx, p))

        #9
        gx = 340
        gy = 580
        ry = 260
        by = 20
        for i in range(3):
            self.Green_Path.append((gx - i*40, gy, 0))
            self.Red_Path.append((gy, ry + i*40, 0))
            self.Blue_Path.append((ry + i*40, by, 0))
            self.Yellow_Path.append((by, gx - i*40, 0))

        #10
        gx = 260
        gy = 540
        ry = 340
        by = 60
        for i in range(5):
            if i == 0:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx, gy - i*40, p))
            self.Red_Path.append((gy - i*40,ry, p))
            self.Blue_Path.append((ry, by - i*40, p))
            self.Yellow_Path.append((by + i*40, gx, p))

        #11
        gx = 220
        gy = 340
        ry = 380
        by = 260
        for i in range(6):
            if i == 3:
                p = 1
            else:
                p = 0
            self.Green_Path.append((gx - i*40, gy, p))
            self.Red_Path.append((gy, ry + i*40, p))
            self.Blue_Path.append((ry - i*40, by, p))
            self.Yellow_Path.append((by, gx + i*40, p))

        #12
        gx = 20
        gy = 300
        ry = 580
        by = 300
        for i in range(6):
            self.Green_Path.append((gx + i*40, gy, 0))
            self.Red_Path.append((gy, ry - i*40, 0))
            self.Blue_Path.append((ry - i*40, by, 0))
            self.Yellow_Path.append((by, gx - i*40, 0))
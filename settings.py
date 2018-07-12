class Color:

    GREEN = '#0CED2C'
    RED = '#F71313'
    YELLOW = '#FFFF00'
    BLUE = '#3575EC'
    DEFAULT = '#E9E9E9'
    CYAN = '#4EB1BA'
    GRAY = '#A9A9A9'


class Board:

    SQUARE_SIZE = 40
    PANEL_WIDTH = 1.5 * Board.SQUARE_SIZE0
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

    green_path = []
    red_path = []
    blue_path = []
    yellow_path = []

    def __init__(self):
        #1
        gx = 1.5 * Board.SQUARE_SIZE
        gy = 0.5 * Board.SQUARE_SIZE
        ry = 13.5 * Board.SQUARE_SIZE
        by = 8.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=0, direction='right')

        #2
        gx = 6.5 * Board.SQUARE_SIZE
        gy = 5.5 * Board.SQUARE_SIZE
        ry = 8.5 * Board.SQUARE_SIZE
        by = 9.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=3, direction='up')

        #3
        gx = 6.5 * Board.SQUARE_SIZE
        gy = 0.5 * Board.SQUARE_SIZE
        ry = 8.5 * Board.SQUARE_SIZE
        by = 14.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=3, direction='right') 

        #4
        gx = 8.5 * Board.SQUARE_SIZE
        gy = 1.5 * Board.SQUARE_SIZE
        ry = 6.5 * Board.SQUARE_SIZE
        by = 13.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=0, direction='down')

        #5
        gx = 9.5 * Board.SQUARE_SIZE
        gy = 6.5 * Board.SQUARE_SIZE
        ry = 20.5 * Board.SQUARE_SIZE
        by = 8.5 * Board.SQUARE_SIZE  
        self.direct(gx, gy, ry, by, count=5, pow_index=3, direction='right')

        #6
        gx = 14.5 * Board.SQUARE_SIZE
        gy = 6.5 * Board.SQUARE_SIZE
        ry = 0.5 * Board.SQUARE_SIZE
        by = 8.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=3, direction='down')

        #7
        gx = 13.5 * Board.SQUARE_SIZE
        gy = 8.5 * Board.SQUARE_SIZE
        ry = 1.5 * Board.SQUARE_SIZE
        by = 6.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=0, direction='left')

        #8
        gx = 9.0 * Board.SQUARE_SIZE
        gy = 9.5 * Board.SQUARE_SIZE
        ry = 6.5 * Board.SQUARE_SIZE
        by = 20.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=3, direction='down')

        #9
        gx = 8.5 * Board.SQUARE_SIZE
        gy = 14.5 * Board.SQUARE_SIZE
        ry = 6.5 * Board.SQUARE_SIZE
        by = 0.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=3, direction='left')

        #10
        gx = 6.5 * Board.SQUARE_SIZE
        gy = 13.5 * Board.SQUARE_SIZE
        ry = 8.5 * Board.SQUARE_SIZE
        by = 1.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=5, pow_index=0, direction='up')

        #11
        gx = 20.5 * Board.SQUARE_SIZE
        gy = 8.5 * Board.SQUARE_SIZE
        ry = 9.5 * Board.SQUARE_SIZE
        by = 6.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=6, pow_index=3, direction='left')

        #12
        gx = 0.5 * Board.SQUARE_SIZE
        gy = 7.5 * Board.SQUARE_SIZE
        ry = 14.5 * Board.SQUARE_SIZE
        by = 7.5 * Board.SQUARE_SIZE
        self.direct(gx, gy, ry, by, count=6, direction='right')

    def right(self, gx, gy, ry, by, count, pow_index=-1):
        for i in range(count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx  +  i*Board.SQUARE_SIZE, gy, p))
            self.red_path.append((gy, ry  -  i*Board.SQUARE_SIZE, p))
            self.blue_path.append((ry - i*Board.SQUARE_SIZE, by, p))
            self.yellow_path.append((by, gx + i*Board.SQUARE_SIZE, p))

    def  left(self, gx, gy, ry, by, count, pow_index=-1):
        for i in range(count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx - i*Board.SQUARE_SIZE, gy, p))
            self.red_path.append((gy, ry + i*Board.SQUARE_SIZE, p))
            self.blue_path.append((ry + i*4, by, p))
            self.yellow_path.append((by, gx - i*Board.SQUARE_SIZE, p))

    def up(self, gx, gy, ry, by, count, pow_index=-1):
        for i in range(count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx, gy - i*Board.SQUARE_SIZE, p))
            self.red_path.append((gy - i*Board.SQUARE_SIZE,ry, p))
            self.blue_path.append((ry, by + i*Board.SQUARE_SIZE, p))
            self.yellow_path.append((by + i*Board.SQUARE_SIZE, gx, p))

    def down(self, gx, gy, ry, by, count, pow_index=-1):
        for i in range(count):
            if i == pow_index:
                p = 1
            else:
                p = 0
            self.green_path.append((gx, gy + i*Board.SQUARE_SIZE, p))
            self.red_path.append((gy + i*Board.SQUARE_SIZE, ry, p))
            self.blue_path.append((ry, by - i*Board.SQUARE_SIZE, p))
            self.yellow_path.append((by - i*Board.SQUARE_SIZE, gx, p))         
    
    def direct(self, gx, gy, ry, by, count, direction, pow_index=-1):
        if direction=='right':
            self.right(gx, gy, ry, by, count, pow_index)
        elif direction=='left':
            self.left(gx, gy, ry, by, count, pow_index)
        elif direction=='down':
            self.down(gx, gy, ry, by, count, pow_index)
        else:
            self.up(gx, gy, ry, by, count, pow_index)    


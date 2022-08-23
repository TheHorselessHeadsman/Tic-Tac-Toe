import pygame as pg

pg.init()

#game variables
width = 750
white = (255,255,255)
black = (0,0,0)
red = (205,51,51)

#setting screen and caption
screen = pg.display.set_mode((width,width))
pg.display.set_caption('Tic_Tac_toe')
font = pg.font.SysFont('Inkfree.tff', 400)
font2 = pg.font.SysFont('Inkfree.tff', 250)


#create game board class for taking user input and storing game date
class Game_Board():
    def __init__(self):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.board_rects = [
            [],
            [],
            []
        ]
        self.btwn = 250
        self.size = 240
        self.final = pg.Surface((width,width))
        for i in self.board_rects:
            for j in range(3):
                i.append(Zone((self.btwn*j)+5, (self.btwn*self.board_rects.index(i))+5, self.size))
    def draw(self):
        [screen.blit(j.surface, (j.x+20, j.y+5)) for i in self.board_rects for j in i]


    def is_over(self, rect, pos):
        return True if rect.collidepoint(pos[0], pos[1]) else False

    def update(self):
        [j.drawchar(1) for i in self.board_rects for j in i if self.board[self.board_rects.index(i)][i.index(j)] == 1]
        [j.drawchar(2) for i in self.board_rects for j in i if self.board[self.board_rects.index(i)][i.index(j)] == 2]
    
    def clickcheck(self):
        global turn
        pos = pg.mouse.get_pos()

        for i in self.board_rects:
            for j in i:
                if self.is_over(j.rect, pos):
                    if self.board[self.board_rects.index(i)][i.index(j)] == 0:
                        self.board[self.board_rects.index(i)][i.index(j)] = turn
                        if turn == 1:
                            turn = 2
                        elif turn == 2:
                            turn = 1
    def checkforwin(self):
        global gameover
        row = 0
        win = 0
        won = False
        for w in range(2):
            row = 0
            y = w+1
            for j in self.board:
                for i in j:
                    if i == y:
                        row += 1
                if row == 3:
                    won = True
                    break
                else:
                    row = 0
            for i in self.board:
                for j in self.board:
                    if j[self.board.index(i)] == y:
                        row += 1
                if row == 3:
                    won = True
                    break
                else:
                    row = 0
            for i in range(3):
                if self.board[i][i] == y:
                    row += 1
            if row == 3:
                won = True
                pass
            else:
                row = 0
                s = 2
                for i in range(3):
                    if self.board[i][s] == y:
                        row +=1
                    s -= 1
                if row ==3:
                    won = True
            if won == True:
                win = w + 1
                break

        if win ==1:
            self.final = font2.render('X WINS!', True, red)
            gameover = True

        if win == 2:
            self.final = font2.render('O WINS!', True, red)
            gameover = True


class Zone():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.rect = pg.rect.Rect(self.x, self.y, size, size)
        self.surface = pg.Surface((size,size))

    def drawchar(self, player):
        player = player
        if player == 1:
            self.surface = font.render('X', True, white, black)
        elif player == 2:
            self.surface = font.render('O', True, white, black)

def drawgrid():
    btwn = width/3
    [pg.draw.line(screen, white, (i*btwn, 0), (i*btwn, width)) for i in range(1,3)]
    [pg.draw.line(screen, white, (0, i*btwn), (width, i*btwn)) for i in range(1,3)]

#redrawing and updating game window
def redrawscreen():
    screen.fill((black))
    gameboard.draw()
    drawgrid()
    if gameover == True:
        screen.blit(gameboard.final, (35,300))
    pg.display.update()

#main gameboard instance
gameboard = Game_Board()
turn = 1
gameover = False

def game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        if gameover == False:
            mouse = pg.mouse.get_pressed()
            if mouse[0]: #when user clicks checks where they clicked
                gameboard.clickcheck()
            gameboard.update()
            gameboard.checkforwin()        
        redrawscreen()

game()
pg.quit()
#Imports
import random
import pygame as pg
import pygame.event


pg.init()


#Variables
p_var = 0
ai_moves = 0
dif = 0
size = width, height = 800, 800
line_size = (100, 100)
line_pos1 = (width / 2, height / 2)
ot_move = 0
color = (50, 0, 200)
rect_color = (200, 255, 255)
mpress = pg.mouse.get_pressed()
sq_left = 9
turn = 1
text = "hi"
done = False


stats = [(), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1)]
scores = ["", 0, 0, 0, 0, 0, 0, 0, 0, 0]
area = [(),(101, 101, 199, 199),(301, 101, 199, 199),(501, 101, 199, 199),(101, 301, 199, 199),(301, 301, 199, 199),(501, 301, 199, 199),(101, 501, 199, 199),(301, 501, 199, 199),(501, 501, 199, 199),]
squares = [(),(size[0]/2+-200, size[1]/2+-200),(size[0]/2+0, size[1]/2+-200),(size[0]/2+200, size[1]/2+-200),(size[0]/2+-200, size[1]/2+0),(size[0]/2+0, size[1]/2+0),(size[0]/2+200, size[1]/2+0),(size[0]/2+-200, size[1]/2+200),(size[0]/2+0, size[1]/2+200),(size[0]/2+200, size[1]/2+200)]


best_move = [0,-111]
pressed = [(), False, False, False, False, False, False, False, False, False]




o_win = False
x_win = False
done2 = False


running = True
BG_color = (100, 0, 0)
line_color = (255 - BG_color[0], 255 - BG_color[1], 255 - BG_color[2])


#Functions


def tot_reset():
   global o_win, x_win, stats, turn, sq_left, pressed
   o_win = False
   x_win = False
   stats = [(), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1)]
   sq_left = 9
   turn = 0
   pressed = [(), False, False, False, False, False, False, False, False, False]
def status_check(clicked, status):
   if turn % 2 == 1:
       status = 1
   elif turn % 2 == 0:
       status = 2
   return status
   detect_win(True)
def draw_symbol(square):
   global turn
   if turn % 2 == 0:
       pygame.draw.circle(screen, line_color, (squares[square[0]], squares[square[1]]), 1, 75)




   elif turn % 2 == 1:
       pg.draw.line(screen, line_color, (square[0] - 75, square[1] - 75), (square[0] + 75, square[1] + 75))
       pg.draw.line(screen, line_color, (square[0] + 75, square[1] - 75), (square[0] - 75, square[1] + 75))
def x_win_text():
   global text
   pygame.display.set_caption('Result')
   font = pygame.font.Font('freesansbold.ttf', 64)
   text = font.render("X's Win!", True, (0, 0, 0), (100, 0, 0))
   textRect = text.get_rect()
   textRect.center = (400, 750)
   while True:
       screen.blit(text, textRect)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pg.quit()
               quit()
           pygame.display.update()
def o_win_text():
   global text
   pygame.display.set_caption('Result')
   font = pygame.font.Font('freesansbold.ttf', 64)
   text = font.render("O's Win!", True, (0, 0, 0), (100, 0, 0))
   textRect = text.get_rect()
   textRect.center = (400, 750)
   while True:
       screen.blit(text, textRect)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pg.quit()
               quit()
           pygame.display.update()
def detect_win(validity):
   global p_var
   global sq_left
   global text
   if stats[1] == 1 and stats[2] == 1 and stats[3] == 1:
       p_var = 1
   elif stats[4] == 1 and stats[5] == 1 and stats[6] == 1:
       p_var = 1
   elif stats[7] == 1 and stats[8] == 1 and stats[9] == 1:
       p_var = 1
   elif stats[1] == 1 and stats[4] == 1 and stats[7] == 1:
       p_var = 1
   elif stats[2] == 1 and stats[5] == 1 and stats[8] == 1:
       p_var = 1
   elif stats[3] == 1 and stats[6] == 1 and stats[9] == 1:
       p_var = 1
   elif stats[1] == 1 and stats[5] == 1 and stats[9] == 1:
       p_var = 1
   elif stats[3] == 1 and stats[5] == 1 and stats[7] == 1:
       p_var = 1
   if stats[1] == 2 and stats[2] == 2 and stats[3] == 2:
       p_var = 2
   elif stats[4] == 2 and stats[5] == 2 and stats[6] == 2:
       p_var = 2
   elif stats[7] == 2 and stats[8] == 2 and stats[9] == 2:
       p_var = 2
   elif stats[1] == 2 and stats[4] == 2 and stats[7] == 2:
       p_var = 2
   elif stats[2] == 2 and stats[5] == 2 and stats[8] == 2:
       p_var = 2
   elif stats[3] == 2 and stats[6] == 2 and stats[9] == 2:
       p_var = 2
   elif stats[1] == 2 and stats[5] == 2 and stats[9] == 2:
       p_var = 2
   elif stats[3] == 2 and stats[5] == 2 and stats[7] == 2:
       p_var = 2
   if validity == True:
       if p_var == 1:
           x_win = True
           x_win_text()
           pg.time.delay(3000)
           pg.quit()
       if p_var == 2:
           o_win = True
           o_win_text()
           pg.time.delay(3000)
           pg.quit()
   elif validity == False:
       if p_var == 1:
           return 1
       if p_var == 2:
           return 2
   if turn > 8:
       pygame.display.set_caption('Result')
       font = pygame.font.Font('freesansbold.ttf', 64)
       text = font.render("It's a Tie!", True, (0, 0, 0), (100, 0, 0))
       textRect = text.get_rect()
       textRect.center = (400, 750)
       while True:
           screen.blit(text, textRect)
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pg.quit()
                   quit()
               pygame.display.update()
   ai_move()
def draw_board():
   pg.draw.line(screen, (line_color), (300, 100), (300, 700))
   pg.draw.aaline(screen, (line_color), (500, 100), (500, 700))
   pg.draw.aaline(screen, (line_color), (100, 300), (700, 300))
   pg.draw.aaline(screen, (line_color), (100, 500), (700, 500))
   pg.display.flip()
def makemove(sq):
   global turn, sq_left
   pressed[sq] = True
   turn += 1
   draw_symbol(squares[sq])
   stats[sq] = status_check(pressed[sq], stats[sq])
   sq_left -= 1
def mouse_pos_check():
   global sq_left
   global turn
   mouse_presses = pygame.mouse.get_pressed()
   done = False
   while done == False:
       draw_board()
       pg.display.flip()
       for event in pg.event.get():
               if event.type == pygame.QUIT:
                   pg.quit()
                   quit()
               if event.type == pygame.MOUSEBUTTONDOWN:
                   mpos = pygame.mouse.get_pos()


               if event.type == pygame.MOUSEBUTTONUP:
                   if event.button == 1 and done == False:
                       if mpos[0] <= 300 and mpos[1] <= 300 and pressed[1] == False:
                           makemove(1)
                           done = True
                       if 300 < mpos[0] <= 500 and mpos[1] <= 300 and not pressed[2]:
                           makemove(2)
                           done = True
                       if 500 < mpos[0]  and mpos[1] <= 300 and not pressed[3]:
                           makemove(3)
                           done = True
                       if mpos[0] <= 300 and 300 < mpos[1] <= 500 and not pressed[4]:
                           makemove(4)
                           done = True
                       if 300 < mpos[0] <= 500 and 300 < mpos[1] <= 500 and not pressed[5]:
                           makemove(5)
                           done = True
                       if 500 < mpos[0]  and 300 < mpos[1] <= 500 and not pressed[6]:
                           makemove(6)
                           done = True
                       if mpos[0] <= 300 and 500 < mpos[1] and not pressed[7]:
                           makemove(7)
                           done = True
                       if 300 < mpos[0] <= 500 and 500 < mpos[1] and not pressed[8]:
                           makemove(8)
                           done = True
                       if 500 < mpos[0] and 500 < mpos[1] and not pressed[9]:
                           makemove(9)
                           done = True
                       detect_win(True)
def ai_move():
   global best_move
   global ot_move
   global sq_left
   global turn
   if sq_left % 2 == ai_moves:
       if dif == 1:
           ot_move = random.randint(1,9)
           if pressed[ot_move] == True:
               ai_move()
           elif pressed[ot_move] == False:
               makemove(ot_move)
               detect_win(True)
        if dif == 2:
           for x in range(1, 9):
               if pressed[x] == False:
                   if detect_win(False) == 1 and ai_moves == 0:
                       scores[x] -= 1
                   if detect_win(False) == 2 and ai_moves == 0:
                       scores[x] += 1
                   if detect_win(False) == 1 and ai_moves == 1:
                       scores[x] += 1
                   if detect_win(False) == 2 and ai_moves == 1:
                       scores[x] -= 1
                   for y in range(1, len(scores)):
                       if scores[y] == best_move[1]:
                           print()
                       elif scores[y] <= best_move[1]:
                           print()
                       elif scores[y] >= best_move[1]:
                           best_move[1] = [scores[x]]
                           best_move[0] = x
               elif pressed[x] == True:
                   scores[x] = -100
       makemove(best_move[0])








#Background
screen = pg.display.set_mode(size)
screen.fill(BG_color)
pygame.display.set_caption('Tic Tac Toe')
pg.display.flip()


pg.draw.line(screen, (line_color), (300, 100), (300, 700))
pg.draw.aaline(screen, (line_color), (500, 100), (500, 700))
pg.draw.aaline(screen, (line_color), (100, 300), (700, 300))
pg.draw.aaline(screen, (line_color), (100, 500), (700, 500))
pg.display.flip()


#Game Loop
while running:
   mouse_pos_check()


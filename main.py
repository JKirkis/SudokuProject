# Author: Conor Arends, Jordan Kerkvliet
# Date Written: 11/09/2023
# Description: User can play sudoku with error checking and an auto solver


# import pygame library
import pygame
import random

# initialise pygame font
pygame.font.init()

# create window
screen = pygame.display.set_mode((500, 620))

# set game title
pygame.display.set_caption("Python Sudoku")
x = 0
y = 0
dif = 500 / 9
val = 0

# create sudoku boards
grids = [
    [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    [
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 3, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]

# get fonts
font1 = pygame.font.SysFont("Calirbi", 40)
font2 = pygame.font.SysFont("Calibri", 20)

# set current game to a random board
current_puzzle = random.choice(grids)


def get_cord(pos):
    global x
    x = pos[0] // dif
    x = int(x)
    global y
    y = pos[1] // dif
    y = int(y)


# highlight selected cell
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw():
    # drawing lines
    for i in range(9):
        for j in range(9):
            if current_puzzle[i][j] != 0:
                # if there is a number in a box, fill it with blue
                pygame.draw.rect(screen, (0, 150, 150), (i * dif, j * dif, dif + 1, dif + 1))

                # fill board with font
                text1 = font1.render(str(current_puzzle[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


def draw_val(val):
    # fill cell with entered value
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


# error messages
def raise_error1():
    text1 = font1.render("Wrong number entered", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Invalid key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# check for valid entry
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# function to solve the puzzle backtracking
def solve(current_puzzle, i, j):
    while current_puzzle[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(current_puzzle, i, j, it) == True:
            current_puzzle[i][j] = it
            global x, y
            x = i
            y = j
            # white color background
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(current_puzzle, i, j) == 1:
                return True
            else:
                current_puzzle[i][j] = 0
            # white color background\
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


# display instructions
def instruction():
    text1 = font2.render("Press R to start a new game", 1, (0, 0, 0))
    text2 = font2.render("Press C to clear", 1, (0, 0, 0))
    text3 = font2.render("Press enter to auto-solve", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))
    screen.blit(text3, (20, 560))


# solved screen
def result():
    text1 = font1.render("You solved the puzzle!", 1, (0, 0, 0))
    screen.blit(text1, (20, 580))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# running game loop
while run:

    # create background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # get mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # set key bindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            #if c is pressed, clear the board
            if event.key == pygame.K_c:
                rs = 0
                error = 0
                flag2 = 0
                current_puzzle = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                # if r is pressed, get a new puzzle
            if event.key == pygame.K_r:
                current_puzzle = random.choice(grids)
                rs = 0
                error = 0
                flag2 = 0
                grid = [[0 for _ in range(9)] for _ in range(9)]

                # Currently not working
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid = [[val for val in row] for row in current_puzzle]

            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                             pygame.K_8, pygame.K_9]:
                val = int(pygame.key.name(event.key))

    if flag2 == 1:
        if solve(current_puzzle, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        # print(x)
        # print(y)
        if valid(current_puzzle, int(x), int(y), val) == True:
            current_puzzle[int(x)][int(y)] = val
            flag1 = 0
        else:
            current_puzzle[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    # update window
    pygame.display.update()

# quit game
pygame.quit()

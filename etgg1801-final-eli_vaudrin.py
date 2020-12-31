# ETGG 1801
# Eli Vaudrin
# Final Lab Option A
# Date 12/28/2020

import pygame as pyg

pyg.init()

gameWindow = pyg.display.set_mode((1000, 800))
pyg.display.set_caption("Lab Final Option A")
clock = pyg.time.Clock()

x = 500
y = 750
width = 17
height = 26
speed = 1

w = (255, 255, 255)
blck = (0, 0, 0)
grn = (14, 204, 40)



isRunning = True

font = pyg.font.Font(None, 26)
txt = font.render("Controls: (Arrow Keys) Up = moves up, Down = move down, Left = move left, Right = move right", isRunning, grn)
txt2 = font.render("Goal: make it to the other side without hitting the other circles", isRunning, grn)

while isRunning:
    gameWindow.fill(blck)

    arwKey = pyg.key.get_pressed()

    if arwKey[pyg.K_LEFT] and x > speed:
        x -= speed
    if arwKey[pyg.K_RIGHT] and x < 1000 - 5 - speed:
        x += speed
    if arwKey[pyg.K_UP] and y > speed:
        y -= speed
    if arwKey[pyg.K_DOWN] and y < 800 - 5 - speed:
        y += speed

    player = pyg.draw.circle(gameWindow, w, (x, y), 10)


    obj = pyg.draw.circle(gameWindow, (255, 187, 0), (500, 100), 35)
    obj2 = pyg.draw.circle(gameWindow, (247, 255, 10), (312, 200), 57)
    obj3 = pyg.draw.circle(gameWindow, (255, 36, 36), (700, 300), 126)
    obj4 = pyg.draw.circle(gameWindow, (255, 125, 5), (215, 597), 189)
    obj5 = pyg.draw.circle(gameWindow, (251, 255, 5), (875, 679), 121)
    obj6 = pyg.draw.circle(gameWindow, (255, 13, 53), (100, 100), 87)
    obj7 = pyg.draw.circle(gameWindow, (255, 162, 0), (939, 237), 49)
    obj8 = pyg.draw.circle(gameWindow, (255, 21, 0), (423, 389), 58)
    obj9 = pyg.draw.circle(gameWindow, (255, 255, 0), (590, 127), 36)
    obj10 = pyg.draw.circle(gameWindow, (255, 153, 0), (497, 578), 47)

    gameWindow.blit(txt, (120, 25))
    gameWindow.blit(txt2, (230, 50))

    for evt in pyg.event.get():
        if evt.type == pyg.QUIT:
            isRunning = False
        elif evt.type == pyg.KEYDOWN:
            if evt.key == pyg.K_ESCAPE:
                isRunning = False


    pyg.display.update()
    clock.tick() / 1000

pyg.quit()


import pygame, sys
import win32api, win32console, win32gui, codecs
import time, random

import math

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GAME')
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
bright_red = (200, 0, 0)
green = (0, 255, 0)
bright_green = (0, 200, 0)

vSR = 0

background = pygame.image.load("C:/Users/Admin/Dropbox/Python/KickBall_background.jpg")
background = pygame.transform.scale(background, (display_width, display_height))

# target = pygame.image.load("C:/Users/Admin/Dropbox/Python/snakehead.png")
# target = pygame.transform.scale(target, (40, 40))

ball = pygame.image.load("C:/Users/Admin/Dropbox/Python/ball.png")
ball = pygame.transform.scale(ball, (40, 40))

pac = pygame.image.load("C:/Users/Admin/Dropbox/Python/ball.png")       #pac is the ball
pac = pygame.transform.scale(pac, (40, 40))

thetaSR = 0
i = 0
# Rotatation of Line
g = 9.81


def gameloop():
    import KickBall
    KickBall.gameloop(v_i, thetaSR)



# def display_target():
#     gameDisplay.blit(target, (10, 500))
#     return 0


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def quitgame():
    pygame.quit()
    quit()


def value_increase():
    smalltext = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects("1", smalltext)
    textRect.center = ((150, 250))
    gameDisplay.blit(textSurf, textRect)


action_called = 0


def button(msg, xpos, ypos, width, height, mouse_on, mouse_off, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global action_called
    if xpos + width > mouse[0] > xpos and ypos + height > mouse[1] > ypos:
        pygame.draw.rect(gameDisplay, mouse_on, (xpos, ypos, width, height))

        if click[0] == 1 and action != None and action_called == 0:
            ########################$$$$$$$$$$$$$$$$$$$#
            #### If mouse is pressed and action_called is equal to 0 then an action will be called whichi wil return a value of 1 or 0
            #### If the action returns 0 then it will be called continuously,
            #### If 1, then it wil not be called again until mouse is released and pressed again
            #########################$$$$$$$$$$$$$$$$$$$
            action_called = action()

        elif (click[0] == 0):
            action_called = 0


    else:
        pygame.draw.rect(gameDisplay, mouse_off, (xpos, ypos, width, height))
    smalltext = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smalltext)
    textRect.center = ((xpos + (width / 2), ypos + (height / 2)))
    gameDisplay.blit(textSurf, textRect)


def theta_increase():
    global thetaSR

    if thetaSR >= 90:
        thetaSR = -1

    thetaSR = round(thetaSR + 2.5, 1)

    #print(thetaSR)
    return 1


def theta_decrease():
    global thetaSR

    if thetaSR <= 0:
        thetaSR = 91

    thetaSR = round(thetaSR - 2.5, 1)

    #print(thetaSR)
    return 1


v_i = 0


def velocity_increase():
    global v_i

    if v_i >= 30:
        v_i = -1

    v_i = v_i + 1

    print(v_i)
    return 1


def velocity_decrease():
    global v_i

    if v_i <= 0:
        v_i = 31

    v_i = v_i - 1

    print(v_i)
    return 1


while True:
    gameDisplay.blit(background, (0, 0))

    gameDisplay.blit(ball, ((0, 500)))

    pygame.event.get()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x_initial = v_i * 4
    y_initial = 0
    theta_rad = thetaSR * math.pi / 180
    x_final = x_initial * math.cos(theta_rad) + y_initial * math.sin(theta_rad)
    y_final = x_initial * math.sin(theta_rad) - y_initial * math.cos(theta_rad)

    t = 2 * (v_i * math.sin(theta_rad)) / 9.8
    x = (v_i * math.cos(theta_rad) * t)

    pygame.draw.circle(gameDisplay, black, (int(x * 10), 540), 5, 1)
    # pygame.draw.circle()

    pygame.draw.line(gameDisplay, green, (0, 540), (10 * x_final, display_height - 10 * y_final - 60), 5)
    button("Hurray!!!", 600, 0, 100, 50, bright_green, green, gameloop)
    button("Quit", 700, 0, 100, 50, bright_red, red, quit)
    button("increase", 0, 0, 100, 25, bright_green, green, velocity_increase)
    button("decrease", 100, 0, 100, 25, bright_green, green, velocity_decrease)
    button("angle increase", 200, 0, 150, 25, bright_green, green, theta_increase)
    button("angle decrease", 350, 0, 150, 25, bright_green, green, theta_decrease)
    button("theta=" + str(thetaSR), 275, 25, 100, 25, green, green)
    button("v_i=" + str(v_i), 50, 25, 60, 25, green, green)

    pygame.display.update()

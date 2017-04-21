import pygame
import sys
import win32api, win32console, win32gui, codecs
import math
import time, random
from pygame.sprite import Sprite
import ProjectileMotion

display_width=800
display_height=600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
gameDisplay= pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


#apple=pygame.image.load("apple.png")


def text_objects1(text, color, size):
    textSurface = medfont.render(text, True, color)
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def pause():
    paused = True

    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue or Q to quit", black, 125)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return 1
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)
#
#
def message_to_screen(msg, color, x_displace=0, size="small"):
    textSurf, textRect = text_objects1(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+x_displace
    gameDisplay.blit(textSurf, textRect)
gameDisplay.fill(white)
pygame.display.update()


def gameloop(v_input,theta_input):


    background = pygame.image.load("C:/Users/Admin/Dropbox/Python/game_background.jpg")
    background = pygame.transform.scale(background, (display_width, display_height))

    blood = pygame.image.load("C:/Users/Admin/Dropbox/Python/blood.png")
    blood = pygame.transform.scale(blood, (60, 60))

    pygame.display.set_caption("Hello there")
    pygame.display.set_icon(background)


    size_target_x=80
    size_target_y=80
    target = pygame.image.load("C:/Users/Admin/Dropbox/Python/goal.png")
    target = pygame.transform.scale(target, (size_target_x, size_target_y))

    pac = pygame.image.load("C:/Users/Admin/Dropbox/Python/ball.png")
    pac = pygame.transform.scale(pac, (40, 40))

    gameDisplay = pygame.display.set_mode((display_width, display_height))

    clock = pygame.time.Clock()

    targetThickness = 40
    dt=0.1
    i=0

    t=[i for i in range(0,1000,1)]
    v=[i for i in range(0,1000,1)]
    x=[i for i in range(0,1000,1)]
    y=[i for i in range(0,1000,1)]
    theta=[i for i in range(0,1000,1)]

    random_int=random.randint(50, 400)
    x[0]=000
    y[0]=500
    v[0]=v_input
    theta[0]=theta_input
    while True:
        i = i + 1
        t[i]=(t[i]/100)
        x_target=700
        y_target=460
        gameDisplay.blit(background, (0,0))

        gameDisplay.blit(target,(x_target,y_target))

        A = ProjectileMotion.projection_object(v[i-1], theta[i-1], x[i-1], y[i-1], .1)

        v[i]=A[0]
        theta[i]=A[1]
        x[i]=x[i-1]+8*A[2]
        y[i]=y[i-1]-8*A[3]
        cy=1*x[i]
        # print("\ntheta")
        # print(theta[0:i])
        if x[i]>display_width-40 :
            b=180
            theta[i]=150
            v[i]=0.7*v[i]

        if 300<x[i]<400 and 450>y[i]>500:
            theta[i]=150
            v[i]=0.7*v[i]


        if x[i] < 0:
            b = 180
            theta[i] = 50
        if y[i] > 500:

            theta[i]=theta_input
            v[i]=0.8*v[i]



        xpos_ball=1*(x[i])
        ypos_ball=1*y[i]
        print(xpos_ball)
        if xpos_ball>800 and ypos_ball>540:
            theta[i]=150
            v[i]=0.7*v[i]


        gameDisplay.blit(pac,(xpos_ball,ypos_ball))

        pygame.draw.line(gameDisplay, green, (0, 500 + 40), (display_width, display_height - 100 + 40), 5)
        pygame.display.update()
        clock.tick(30)
        print("")
        print("")



        if xpos_ball>x_target-size_target_x/4 and xpos_ball<x_target+size_target_x/2 and ypos_ball>y_target:
            message_to_screen("you scored", black, 150, "largefont")
            pygame.display.update()
            a = 1
            a = pause()


            if a == 1:
                i = 0
                x = 0
                y = 0

                t = 0
                break

        if i > 999 or ypos_ball > 600 or v[i]<0.8:
            i = 0
            message_to_screen("you Missed", green, 150, "largefont")
            pygame.display.update()
            a = 1
            a = pause()
            if a == 1:
                i = 0

                break




        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
    #clock.tick(FPS)
# gameloop()

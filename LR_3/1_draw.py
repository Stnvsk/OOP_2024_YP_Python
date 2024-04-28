import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

screen.fill(white)


def body(surface, color1, color2):
    list = [[200, 200], [200, 200], [150, 150], [0, 1]]
    for i in range(0, 2, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eye_left(surface, color1, color2):
    list = [[130, 130, 130], [150, 150, 150], [30, 30, 10], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eye_right(surface, color1, color2):
    list = [[260, 260, 260], [150, 150, 150], [20, 20, 10], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eyebrow(surface, color):
    list = [[70, 85, 185, 170], [50, 35, 135, 150]]
    list1 = [[345, 335, 215, 220], [100, 85, 135, 150]]
    for i in range(0,1,1):
        polygon(surface, color, [(list[0][i], list[1][i]), (list[0][i+1], list[1][i+1]), (list[0][i+2], list[1][i+2]),
                                 (list[0][i+3], list[1][i+3])])
        polygon(surface, color,
                [(list1[0][i], list1[1][i]), (list1[0][i + 1], list1[1][i + 1]), (list1[0][i + 2], list1[1][i + 2]),
                 (list1[0][i + 3], list1[1][i + 3])])


body(screen, yellow, black)
rect(screen, black, (120, 270, 155, 30)) #прямоугольник (рот)
eye_left(screen, red, black)
eye_right(screen, red, black)
eyebrow(screen, black)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
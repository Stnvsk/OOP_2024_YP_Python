import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((1000, 600))

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
beige = (255, 218, 185)
blue = (135, 206, 250)
orange = (255, 140, 0)
saddleBrown = (139, 69, 19)
green = (0, 255, 0)
darkGreen = (0, 100, 0)
violet = (148, 0, 211)
LightGray = (211, 211, 211)


screen.fill(white)


def body(color, color1, color2):
    polygon(screen, color2, [(885, 200), (865, 200), (785, 500), (805, 500)])
    polygon(screen, color2, [(515, 200), (535, 200), (615, 500), (595, 500)])
    circle(screen, color, (700, 570), 150)
    rect(screen, color1, (0, 570, 900, 600))
    ellipse(screen, color2, (600, 200, 200, 250))
    polygon(screen, orange, [(610, 415), (560, 435), (560, 490), (615, 505), (640, 455)])
    polygon(screen, black, [(610, 415), (560, 435), (560, 490), (615, 505), (640, 455)], 1)
    polygon(screen, orange, [(790, 415), (840, 435), (840, 490), (785, 505), (760, 455)])
    polygon(screen, black, [(790, 415), (840, 435), (840, 490), (785, 505), (760, 455)], 1)


def body2(color, color1, color2):
    polygon(screen, color2, [(485, 200), (465, 200), (385, 500), (405, 500)])
    polygon(screen, color2, [(115, 200), (135, 200), (215, 500), (195, 500)])
    circle(screen, color, (300, 570), 150)
    rect(screen, color1, (0, 570, 600, 600))
    ellipse(screen, color2, (200, 200, 200, 250))
    polygon(screen, color, [(210, 415), (160, 435), (160, 490), (215, 505), (240, 455)])
    polygon(screen, black, [(210, 415), (160, 435), (160, 490), (215, 505), (240, 455)], 1)
    polygon(screen, color, [(390, 415), (440, 435), (440, 490), (385, 505), (360, 455)])
    polygon(screen, black, [(390, 415), (440, 435), (440, 490), (385, 505), (360, 455)], 1)


def hands(color1, color2):
    ellipse(screen, color1, (503, 150, 48, 60))
    ellipse(screen, color2, (503, 150, 48, 60), 1)
    ellipse(screen, color1, (849, 150, 48, 60))
    ellipse(screen, color2, (849, 150, 48, 60), 1)


def hands2(color1, color2):
    ellipse(screen, color1, (103, 150, 48, 60))
    ellipse(screen, color2, (103, 150, 48, 60), 1)
    ellipse(screen, color1, (449, 150, 48, 60))
    ellipse(screen, color2, (449, 150, 48, 60), 1)


def eye_left(surface, color1, color2):
    list = [[660, 660, 660], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eye_left2(surface, color1, color2):
    list = [[260, 260, 260], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eye_right(surface, color1, color2):
    list1 = [[740, 740, 740], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list1[0][i], list1[1][i]), list1[2][i], list1[3][i])
        color1 = color2


def eye_right2(surface, color1, color2):
    list1 = [[340, 340, 340], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list1[0][i], list1[1][i]), list1[2][i], list1[3][i])
        color1 = color2


def nose(surface, color1, color2):
    list = [[690, 710, 700], [330, 330, 350], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def nose2(surface, color1, color2):
    list = [[290, 310, 300], [330, 330, 350], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def mouth(surface, color1, color2):
    list = [[650, 750, 700], [360, 360, 400], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def mouth2(surface, color1, color2):
    list = [[250, 350, 300], [360, 360, 400], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def hair():
    polygon(screen, violet, [(720, 175), (700, 200), (725, 205)])
    polygon(screen, black, [(720, 175), (700, 200), (725, 205)], 1)
    polygon(screen, violet, [(750, 185), (725, 205), (745, 215)])
    polygon(screen, black, [(750, 185), (725, 205), (745, 215)], 1)
    polygon(screen, violet, [(770, 200), (745, 215), (765, 230)])
    polygon(screen, black, [(770, 200), (745, 215), (765, 230)], 1)
    polygon(screen, violet, [(795, 220), (765, 230), (780, 250)])
    polygon(screen, black, [(795, 220), (765, 230), (780, 250)], 1)
    polygon(screen, violet, [(815, 250), (780, 250), (790, 275)])
    polygon(screen, black, [(815, 250), (780, 250), (790, 275)], 1)
    polygon(screen, violet, [(680, 175), (700, 200), (675, 205)])
    polygon(screen, black, [(680, 175), (700, 200), (675, 205)], 1)
    polygon(screen, violet, [(650, 185), (675, 205), (655, 215)])
    polygon(screen, black, [(650, 185), (675, 205), (655, 215)], 1)
    polygon(screen, violet, [(630, 200), (655, 215), (635, 230)])
    polygon(screen, black, [(630, 200), (655, 215), (635, 230)], 1)
    polygon(screen, violet, [(605, 220), (635, 230), (620, 250)])
    polygon(screen, black, [(605, 220), (635, 230), (620, 250)], 1)
    polygon(screen, violet, [(585, 250), (620, 250), (610, 275)])
    polygon(screen, black, [(585, 250), (620, 250), (610, 275)], 1)


def hair2():
    polygon(screen, yellow, [(320, 175), (300, 200), (325, 205)])
    polygon(screen, black, [(320, 175), (300, 200), (325, 205)], 1)
    polygon(screen, yellow, [(350, 185), (325, 205), (345, 215)])
    polygon(screen, black, [(350, 185), (325, 205), (345, 215)], 1)
    polygon(screen, yellow, [(370, 200), (345, 215), (365, 230)])
    polygon(screen, black, [(370, 200), (345, 215), (365, 230)], 1)
    polygon(screen, yellow, [(395, 220), (365, 230), (380, 250)])
    polygon(screen, black, [(395, 220), (365, 230), (380, 250)], 1)
    polygon(screen, yellow, [(415, 250), (380, 250), (390, 275)])
    polygon(screen, black, [(415, 250), (380, 250), (390, 275)], 1)
    polygon(screen, yellow, [(280, 175), (300, 200), (275, 205)])
    polygon(screen, black, [(280, 175), (300, 200), (275, 205)], 1)
    polygon(screen, yellow, [(250, 185), (275, 205), (255, 215)])
    polygon(screen, black, [(250, 185), (275, 205), (255, 215)], 1)
    polygon(screen, yellow, [(230, 200), (255, 215), (235, 230)])
    polygon(screen, black, [(230, 200), (255, 215), (235, 230)], 1)
    polygon(screen, yellow, [(205, 220), (235, 230), (220, 250)])
    polygon(screen, black, [(205, 220), (235, 230), (220, 250)], 1)
    polygon(screen, yellow, [(185, 250), (220, 250), (210, 275)])
    polygon(screen, black, [(185, 250), (220, 250), (210, 275)], 1)


def man1():
    body(orange, white, beige)
    eye_left(screen, blue, black)
    eye_right(screen, blue, black)
    nose(screen, saddleBrown, black)
    mouth(screen, red, black)
    hands(beige, white)
    hair()


def man2():
    body2(darkGreen, white, beige)
    eye_left2(screen, LightGray, black)
    eye_right2(screen, LightGray, black)
    nose2(screen, saddleBrown, black)
    mouth2(screen, red, black)
    hands2(beige, white)
    hair2()


def tablet():
    rect(screen, green, (80, 100, 840, 70))
    rect(screen, black, (80, 100, 840, 70), 1)
    font = pygame.font.SysFont('montserrat black', 45)
    text = font.render(str('PYTHON is REALLY AMAZING!'), True, black)
    screen.blit(text, (150, 110))


man1()
man2()
tablet()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
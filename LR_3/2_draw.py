import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 600))

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
beige = (255, 218, 185)
blue = (135, 206, 250)
orange = (255, 140, 0)
saddleBrown = (139, 69, 19)
green = (0, 255, 0)
violet = (148, 0, 211)

screen.fill(white)


def body(color, color1, color2):
    polygon(screen, color2, [(585, 200), (565, 200), (485, 500), (505, 500)])
    polygon(screen, color2, [(215, 200), (235, 200), (315, 500), (295, 500)])
    circle(screen, color, (400, 570), 150)
    rect(screen, color1, (0, 570, 600, 600))
    ellipse(screen, color2, (300, 200, 200, 250))
    polygon(screen, orange, [(310, 415), (260, 435), (260, 490), (315, 505), (340, 455)])
    polygon(screen, black, [(310, 415), (260, 435), (260, 490), (315, 505), (340, 455)], 1)
    polygon(screen, orange, [(490, 415), (540, 435), (540, 490), (485, 505), (460, 455)])
    polygon(screen, black, [(490, 415), (540, 435), (540, 490), (485, 505), (460, 455)], 1)


def hands(color1, color2):
    ellipse(screen, color1, (203, 150, 48, 60))
    ellipse(screen, color2, (203, 150, 48, 60), 1)
    ellipse(screen, color1, (549, 150, 48, 60))
    ellipse(screen, color2, (549, 150, 48, 60), 1)


def eye_left(surface, color1, color2):
    list = [[360, 360, 360], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list[0][i], list[1][i]), list[2][i], list[3][i])
        color1 = color2


def eye_right(surface, color1, color2):
    list1 = [[440, 440, 440], [300, 300, 300], [20, 20, 7], [0, 1, 0]]
    for i in range(0, 3, 1):
        circle(surface, color1, (list1[0][i], list1[1][i]), list1[2][i], list1[3][i])
        color1 = color2


def nose(surface, color1, color2):
    list = [[390, 410, 400], [330, 330, 350], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def mouth(surface, color1, color2):
    list = [[350, 450, 400], [360, 360, 400], [0, 1]]
    for i in range(0, 2, 1):
        polygon(surface, color1, [(list[0][0], list[1][0]), (list[0][1], list[1][1]), (list[0][2], list[1][2])], list[2][i])
        color1 = color2


def hair():
    polygon(screen, violet, [(420, 175), (400, 200), (425, 205)])
    polygon(screen, black, [(420, 175), (400, 200), (425, 205)], 1)
    polygon(screen, violet, [(450, 185), (425, 205), (445, 215)])
    polygon(screen, black, [(450, 185), (425, 205), (445, 215)], 1)
    polygon(screen, violet, [(470, 200), (445, 215), (465, 230)])
    polygon(screen, black, [(470, 200), (445, 215), (465, 230)], 1)
    polygon(screen, violet, [(495, 220), (465, 230), (480, 250)])
    polygon(screen, black, [(495, 220), (465, 230), (480, 250)], 1)
    polygon(screen, violet, [(515, 250), (480, 250), (490, 275)])
    polygon(screen, black, [(515, 250), (480, 250), (490, 275)], 1)
    polygon(screen, violet, [(380, 175), (400, 200), (375, 205)])
    polygon(screen, black, [(380, 175), (400, 200), (375, 205)], 1)
    polygon(screen, violet, [(350, 185), (375, 205), (355, 215)])
    polygon(screen, black, [(350, 185), (375, 205), (355, 215)], 1)
    polygon(screen, violet, [(330, 200), (355, 215), (335, 230)])
    polygon(screen, black, [(330, 200), (355, 215), (335, 230)], 1)
    polygon(screen, violet, [(305, 220), (335, 230), (320, 250)])
    polygon(screen, black, [(305, 220), (335, 230), (320, 250)], 1)
    polygon(screen, violet, [(285, 250), (320, 250), (310, 275)])
    polygon(screen, black, [(285, 250), (320, 250), (310, 275)], 1)


def tablet():
    rect(screen, green, (180, 100, 440, 70))
    rect(screen, black, (180, 100, 440, 70), 1)
    font = pygame.font.SysFont('roboto', 45, bold = True)
    text = font.render(str('PYTHON is AMAZING'), True, black)
    screen.blit(text, (180, 110))


body(orange, white, beige)
eye_left(screen, blue, black)
eye_right(screen, blue, black)
nose(screen, saddleBrown, black)
mouth(screen, red, black)
hands(beige, white)
tablet()
hair()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
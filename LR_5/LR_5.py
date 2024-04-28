import pygame
from pygame.draw import *
from random import randint

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1280, 800))
RED = (255, 69, 0)
BLUE = (138, 43, 226)
YELLOW = (255, 215, 0)
GREEN = (0, 255, 127)
MAGENTA = (255, 20, 147)
CYAN = (0, 191, 255)
BLACK = (8, 0, 44)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

num_of_balls = 15  # кол-во шаров на экране
balls = []  # Список для хранения параметров созданных шаров


def new_ball():
    """ Функция создает параметры шара на экране на случайных координатах
    со случайным радиусом, цветом и шагом перемещения """

    # создание случайных координат по х, у и размер радиуса
    x, y, r = randint(100, 1180), randint(100, 700), randint(10, 50)
    color = COLORS[randint(0, 5)]  # случайный выбор цвета
    dx, dy = randint(-5, 5), randint(-5, 5)  # случайный шаг по х, у
    return [x, y, r, color, dx, dy]  # возврат выбранных значений


def draw_ball(ball):
    """ Функция рисует шар с параметрами созданами в функции new_ball"""

    circle(screen, ball[3], (ball[0], ball[1]), ball[2])


def move(ball):
    """ Функция передвигает шар в ограниченной экраном области """

    ball[0] += ball[4]  # к координате х прибавляется шаг по х (dx)
    ball[1] += ball[5]  # к координате у прибавляется шаг по у (dy)
    if ball[0] - ball[2] < 0 or ball[0] + ball[2] > 1280:
        ball[4] = - ball[4]  # к шагу по х (dx) добавляется минус, чтобы идти в другом направлении
    if ball[1] - ball[2] < 0 or ball[1] + ball[2] > 750:
        ball[5] = -ball[5]  # к шагу по у (dy) добавляется минус, чтобы идти в другом направлении


def check_clik(event, ball):
    """ Функция проверяет координаты нажатие ПКМ и координаты шара для возможности засчитать попадане """

    result = ((event.pos[0] - ball[0]) ** 2 + (event.pos[1] - ball[1]) ** 2) ** 0.5
    return result < ball[2]  # возвращает значение меньше радиуса круга


def score():
    """ Функция создает текст Счёт: и выводит количество попаданий на экран"""

    font = pygame.font.SysFont('roboto', 35, bold=True)  # задание параметров шрифта
    text = font.render(str('Счет:'), True, WHITE)  # надпись Счёт:
    screen.blit(text, (20, 750))  # отображения текста на координатах
    text = font.render(str(count_goals), True, WHITE)  # отображение количества очков
    screen.blit(text, (120, 750))  # отображения текста на координатах


for i in range(num_of_balls):
    """ Создается количество шаров записанных в num_of_balls, и параметры этих шаров записывают в список balls """
    balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False
count_goals = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if check_clik(event, ball):  # если есть попадание, то добавляется очко
                    count_goals += 1
                    balls.remove(ball)  # убирается шар, в который папали
                    balls.append(new_ball())  # создается новый шар
    for ball in balls:
        draw_ball(ball)
        move(ball)
    score()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('-------------------------')
print('Количество попаданий:', count_goals - 1)

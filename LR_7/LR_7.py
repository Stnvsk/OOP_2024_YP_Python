from random import randrange as rnd, choice
from tkinter import *
import math
import time

# Настройка окна программы
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

"""Класс ball описывает снаряды"""


class ball():
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = 'gray'
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 10

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """
        Метод передвижения снаряда и его физика
        """
        if self.y <= 500:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779

    def hittest(self, tar):
        """
        Метод проверки попадания снарядом в шар
        """
        if abs(tar[0] - self.x) <= (self.r + tar[2]) and abs(tar[1] - self.y) <= (self.r + tar[2]):
            return True
        else:
            return False


"""
Класс gun описывает пушку. 
"""


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(0, 0, 0, 0, width=7)

    def new_gun(self):
        x0 = self.x0 = 20
        y0 = self.y0 = 450
        x = self.x = 50
        y = self.y = 420
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        return [x0, y0, x, y, dx, dy]

    def draw_gun(self, list):
        canv.coords(self.id, list[0], list[1], list[2], list[3])
        canv.itemconfig(self.id, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Метод окончания стрельбы и возврат к начальным настройкам
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Метод наводки пушки за курсором
        """
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        """
        Метод силы стрельбы
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


"""
Класс target описывает цель. 
"""


class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.live = 1

    def new_target(self):
        """
        Метод возвращающий списком параметры цели
        """
        x = self.x = rnd(100, 740)
        y = self.y = rnd(100, 540)
        r = self.r = rnd(10, 50)
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        color = self.color = choice(['green'])
        return [x, y, r, color, dx, dy]

    def draw_target(self, tar):
        canv.coords(self.id, tar[0] - tar[2], tar[1] - tar[2], tar[0] + tar[2], tar[1] + tar[2])
        canv.itemconfig(self.id, fill=tar[3])

    def hit(self, tar, points=1):
        """
        Метод зачитывающий попадания по цели
        """
        if tar[3] == 'red' or tar[3] == 'green':
            tar[0] = 0
            tar[1] = 0
            tar[2] = 0
            tar[3] = ''
            tar[4] = 0
            tar[5] = 0
            self.points += points
            canv.itemconfig(self.id_points, text=self.points)
        if tar[3] == 'yellow':
            tar[0] = 0
            tar[1] = 0
            tar[2] = 0
            tar[3] = ''
            tar[4] = 0
            tar[5] = 0
            tar[6] = 0
            self.points += points
            canv.itemconfig(self.id_points, text=self.points)


"""
Два новых типа целей с разным характером поведением
________________________________________________________________________________________________________________________
"""


class fast_target(target):
    def new_target(self):
        x = self.x = rnd(100, 740)
        y = self.y = rnd(100, 540)
        r = self.r = rnd(5, 10)
        dx = self.dx = rnd(6, 15)
        dy = self.dy = rnd(6, 15)
        color = self.color = 'red'
        return [x, y, r, color, dx, dy]


class unstable_target(target):
    def new_target(self):
        x = self.x = rnd(100, 740)
        y = self.y = rnd(100, 540)
        r = self.r = rnd(10, 30)
        dx = self.dx = rnd(1, 5)
        dy = self.dy = rnd(1, 5)
        dr = self.dr = rnd(-9, 9)
        color = self.color = 'yellow'
        return [x, y, r, color, dx, dy, dr]


"""
В ходе рефакторинга созданы три функции для облегчения основной функции игры
________________________________________________________________________________________________________________________
"""


def move_target(tar):
    """
    Функция двигает определенную цель в области окна программы
    """
    if tar[3] == 'red' or tar[3] == 'green':
        tar[0] += tar[4]
        tar[1] += tar[5]
        if tar[0] - tar[2] < 0 or tar[0] + tar[2] > 800:
            tar[4] = - tar[4]
        if tar[1] - tar[2] < 0 or tar[1] + tar[2] > 600:
            tar[5] = - tar[5]
    if tar[3] == 'yellow':
        tar[0] += tar[4]
        tar[1] += tar[5]
        tar[2] += tar[6]
        if tar[0] - tar[2] < 0 or tar[0] + tar[2] > 800:
            tar[4] = - tar[4]
        if tar[1] - tar[2] < 0 or tar[1] + tar[2] > 600:
            tar[5] = - tar[5]
        if tar[2] < 2:
            tar[2] += 5
        if tar[2] > 50:
            tar[2] -= 30


def die_target(object, tar):
    """
    Смерть определенной цели при попадании
    """
    if tar[3] == 'red' or tar[3] == 'green':
        object.live = 0
        object.hit(tar)
    else:
        object.live = 0
        object.hit(tar)


def move_target_in_window(object, tar):
    """
    Функция для передвижения цели в окне программы
    """
    for _ in tar:
        object.draw_target(tar)
        move_target(tar)


"""
________________________________________________________________________________________________________________________
"""

''''def move_gun(list):
    list[0] += list[4]
    list[1] += list[5]
    list[2] += list[4]
    list[3] += list[5]
    if list[0] < 0 or list[0] > 800:
        list[4] = - list[4]
    if list[1] < 0 or list[1] > 600:
        list[5] = - list[5]


def move_gun_in_window(object, list):
    for _ in list:
        object.draw_gun(list)
        move_gun(list)'''

# Инициальзация объектов
tar = target()  # Обычная цель (зеленая)
f_tar = fast_target()  # Быстрая цель (красная)
uns_tar = unstable_target()  # Нестабильная цель (желтая)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    """
    Основная функция игры
    """
    global gun, tar, t2, g1, f_tar, uns_tar, screen1, balls, bullet
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    tar.live = 1
    f_tar.live = 1
    uns_tar.live = 1
    # gun_list = g1.new_gun()
    tar1_list = tar.new_target()
    ft1_list = f_tar.new_target()
    uns_t1_list = uns_tar.new_target()
    while tar.live or f_tar.live or uns_tar.live or balls:
        for b in balls:
            b.move()
            if b.hittest(tar1_list) and tar.live:
                die_target(tar, tar1_list)
            if b.hittest(ft1_list) and f_tar.live:
                die_target(f_tar, ft1_list)
            if b.hittest(uns_t1_list) and uns_tar.live:
                die_target(uns_tar, uns_t1_list)
            if tar.live == 0 and f_tar.live == 0 and uns_tar.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
        # move_gun_in_window(g1, gun_list)
        move_target_in_window(tar, tar1_list)
        move_target_in_window(f_tar, ft1_list)
        move_target_in_window(uns_tar, uns_t1_list)
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
mainloop()

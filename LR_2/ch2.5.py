from random import randint
import turtle

def bump(crd, nmb):
    for i in range(len(crd)):
        if i == nmb:
            continue
        else:
            if crd[i][0] == crd[nmb][0] and crd[i][1] == crd[nmb][1]:
                return i
    return -1

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.goto(-200, 200)
turtle.penup()

num = 25
steps = 1000
cord = list([0, 0] for i in range(num))
speed = [[randint(-15, 15), randint(-15, 15)] for i in range(num)]
pool = [turtle.Turtle(shape='circle') for i in range(num)]
i = 0
for unit in pool:
    unit.penup()
    cord[i] = [randint(-150, 150), randint(-150, 150)]
    unit.goto(cord[i])
    i += 1
for i in range(steps):
    for u in range(num):
        if cord[u][0] >= 200 - speed[u][0] or cord[u][0] <= -200 + speed[u][0]:
            speed[u][0] = -speed[u][0]
        if cord[u][1] >= 200 - speed[u][1] or cord[u][1] <= -200 + speed[u][1]:
            speed[u][1] = -speed[u][1]
        if bump(cord, u):
            j = bump(cord, u)
            speed[u], speed[j] = speed[j], speed[u]
            cord[u][0], cord[u][1] =  cord[u][0] + 1, cord[u][1] + 1
        cord[u][0], cord[u][1] = cord[u][0] + speed[u][0], cord[u][1] + speed[u][1]
        pool[u].goto(cord[u])
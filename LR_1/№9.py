import turtle
turtle.shape('turtle')
import math

def figura (a, n):
    i = 0
    u = 360/n
    for i in range(n):
        turtle.forward(a)
        turtle.right(u)

def mng(n):
    turtle.left(180 / n)
    for i in range(n):
        turtle.forward(n * 5)
        turtle.left(360 / n)
    turtle.right(180 / n)

turtle.left(90)
for i in range(3, 13):
    a = i * 5
    turtle.penup()
    turtle.goto((a / (2 * math.sin(math.pi / i))), 0)
    turtle.pendown()
    mng(i)


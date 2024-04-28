from random import randint
import turtle

def left_right():
    num = randint(1, 100)
    an = randint(0, 360)
    d = randint(1, 50)
    if num < 50:
        turtle.right(an)
    else:
        turtle.right(an)
    turtle.forward(d)

turtle.shape('turtle')
turtle.tracer(2)
i = 0
while i < 100:
    left_right()
    i += 1
turtle.done()
import turtle
turtle.shape('turtle')
def circle(r):
    i = 0
    j = 0
    while i <= 360:
        turtle.forward(r)
        turtle.left(1)
        i += 1
    while j <= 360:
        turtle.forward(r)
        turtle.right(1)
        j += 1
i = 0
x = 6
r = 1
turtle.tracer(2)
turtle.right(90)
while i < x:
    circle(r)
    turtle.right(180)
    i += 1
    r += 0.1

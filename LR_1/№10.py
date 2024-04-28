import turtle
turtle.shape('turtle')
def circle():
    i = 0
    while i <= 360:
        turtle.forward(1)
        turtle.left(1)
        i += 1
i = 0
x = 12
y = 360/x
turtle.tracer(2)
while i < x:
    circle()
    turtle.left(y)
    i += 1

import turtle
turtle.shape('turtle')
i = 0
a = 10
while i < 10:
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(135)
    i += 1
    a += 15

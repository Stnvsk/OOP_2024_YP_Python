import turtle
turtle.shape('turtle')
n = 6
i = 0
a = 360/n
while i < n:
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(180)
    turtle.right(a)
    i += 1

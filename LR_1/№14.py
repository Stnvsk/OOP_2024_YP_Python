import turtle
turtle.shape('turtle')
def star(n):
    for i in range(n):
        turtle.forward(200)
        turtle.right(180 - 180/n)

turtle.penup()
turtle.backward(200)
turtle.pendown()
star(5)
turtle.penup()
turtle.forward(300)
turtle.pendown()
star(11)
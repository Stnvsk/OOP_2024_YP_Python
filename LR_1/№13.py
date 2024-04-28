import turtle
turtle.shape('turtle')
def circle(r):
    i = 0
    while i <= 360:
        turtle.forward(r)
        turtle.left(1)
        i += 1
def spiral (r, w, c):
    turtle.pendown()
    turtle.width(w)
    turtle.color(color)
    i = 0
    while i < 80:
        turtle.forward(r)
        turtle.right(1)
        i += 1
    turtle.penup()
def fill_circle(r, color):
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    circle(r)
    turtle.end_fill()
    turtle.penup()
def no_fill_circle(r, w, color):
    turtle.pendown()
    turtle.width(w)
    turtle.color(color)
    i = 0
    while i <= 360:
        turtle.forward(r)
        turtle.left(1)
        i += 1
    turtle.penup()

turtle.tracer(2)
i = 0
r = 2
w = 3
color = "yellow"
fill_circle(r, color)
color = "brown"
no_fill_circle(r, w, color)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
r = 0.4
color = "white"
fill_circle(r, color)
color = "brown"
w = 2
no_fill_circle(r, w, color)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
r = 0.25
color = "black"
fill_circle(r, color)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
r = 0.4
turtle.right(90)
turtle.forward(95)
turtle.left(90)
color = "white"
fill_circle(r, color)
color = "brown"
no_fill_circle(r, w, color)
r = 0.25
color = "black"
fill_circle(r, color)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
r = 0.4
turtle.left(180)
turtle.forward(90)
turtle.right(90)
turtle.forward(35)
turtle.left(45)
r = 1
color = "brown"
spiral(r, w, color)

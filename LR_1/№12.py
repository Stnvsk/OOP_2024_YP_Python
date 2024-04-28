import turtle
turtle.shape('turtle')
def spiral (n):
    i = 0
    j = 0
    while i < 180:
        turtle.forward(0.8)
        turtle.right(1)
        i += 1
    while j < 180:
        turtle.forward(0.1)
        turtle.right(1)
        j += 1
turtle.tracer(2)
n = 10
i = 0
turtle.left(90)
while i <= n:
    spiral(n)
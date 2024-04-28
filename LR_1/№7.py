import turtle
turtle.shape('turtle')
i = 0
turtle.tracer(2)
while i <= 10000:
    turtle.forward(0.001+i)
    turtle.left(1)
    i += 0.001
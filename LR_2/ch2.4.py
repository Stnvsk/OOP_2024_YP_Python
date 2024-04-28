import turtle
turtle.tracer(2)
turtle.shape('circle')
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
x, y = -400, 0
vx, vy = 10, 90
a = -9.81
for t in range(8000):
    if y <= 0:
        vy = abs(vy)*0.8
    x += vx * 0.01
    y += vy * 0.01 + a * 0.01 ** 2 / 2
    vy += a * 0.01
    turtle.goto(x, y)
turtle.update()
turtle.done()
import turtle
turtle.shape('turtle')

def goto (i,j):
    turtle.penup()
    turtle.goto(i,j)
    turtle.pendown()

def numbers():
    goto(0, 0)
    goto(-300,200)
    x = -275
    y = 300
    list = [(0,90,100, 135, 70.72, 135)]
    list1 = [(50, -90, 50, -45, 70.72, 135, 50),(50, -135, 70.72, 135, 50, -135, 70.72, 135),(0,-90,50,90,50,-90,50,180,100,-90),(50, 180, 50, 90, 50, 90, 50, -90, 50, -90, 50, 180)]
    list3 = [(0,-135,70.72,45,50,90,50,90,50,90,50,180),(50,-135,70.72,45,50,90),(50,-90,50,-90,50,90,50,90,50,90,50,90,50,-90,50,-90),(0, -90, 50, 90, 50, -135, 70.72, 180, 70.72, 45, 50, 90, 50,180),(50,-90,100,-90,50,-90,100,-90)]
    for i in list:
        for j in range(len(i)):
            if j % 2 != 1:
                turtle.forward(i[j])
            else:
                turtle.left(i[j])
        goto(x, y)
    for i in list1:
        x += 75
        for j in range(len(i)):
            if j % 2 != 1:
                turtle.forward(i[j])
            else:
                turtle.left(i[j])
        goto(x, y)
    goto(75, y)
    for i in list3:
        x += 75
        for j in range(len(i)):
            if j % 2 != 1:
                turtle.forward(i[j])
            else:
                turtle.left(i[j])
        goto(x, y)

def index():
    goto(-300,0)
    x = -275
    y = 100
    list = [(0, 90, 100, 135, 70.72, 135)]
    list1 = [(50, -90, 50, -45, 70.72, 135, 50), (50, 180, 50, 90, 50, 90, 50, -90, 50, -90, 50, 180),
             (50, -90, 50, -45, 70.72, 135, 50), (50, -135, 70.72, 135, 50, -135, 70.72, 135),
             (0, -90, 50, 90, 50, -135, 70.72, 180, 70.72, 45, 50, 90, 50, -90)]
    for i in list:
        for j in range(len(i)):
            if j % 2 != 1:
                turtle.forward(i[j])
            else:
                turtle.left(i[j])
        goto(x, y)

    for i in list1:
        x += 75
        for j in range(len(i)):
            if j % 2 != 1:
                turtle.forward(i[j])
            else:
                turtle.left(i[j])
        goto(x, y)

turtle.tracer(1)
numbers()
index()

turtle.done()
import turtle
turtle.shape('turtle')

f = open('цифры.txt', 'r')
writer = [0]*10
for i in range(10):
    s = list(map(int, f.readline().split()))
    mind = [0]*(len(s) // 2)
    for j in range(0, len(s), 2):
        mind[j // 2] = [s[j], s[j+1]]
    writer[i] = mind
print('Введите индекс без пробелов')
ind = str(int(input()))
mind = [0]*len(ind)
for i in range(len(ind)):
    mind[i] = int(ind[i])
x, y, xend = 0, 0, 0
for i in range(len(ind)):
    xend = x + 30
    if mind[i] == 1:
        y -= 20
    elif mind[i] == 6:
        x += 20
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(len(writer[mind[i]])):
        turtle.goto(x + writer[mind[i]][j][0], writer[mind[i]][j][1])
    turtle.penup()
    y = 0
    x = xend

turtle.done()
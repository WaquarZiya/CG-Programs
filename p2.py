import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(10)

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.circle(radius)

def translate(x, y, dx, dy):
    return x + dx, y +dy

def rotate(angle):
    t.setheading(angle)

def scale(x, y, sx, sy):
    return x * sx, y * sy

draw_rectangle(-200, -200, 100, 50, 'red')
tx, ty = translate(-200, -200, 200, 0)
draw_rectangle(tx, ty, 100, 50, 'orange')
scale(-200, -200, 2, 2)
draw_rectangle(200, -200, 200, 100, 'green')
rotate(45)
draw_rectangle(-400, -200, 100, 50, 'yellow')

draw_circle(-200, 100, 50, 'blue')
tx, ty = translate(-200, 100, 200, 0)
draw_circle(tx, ty, 50, 'cyan')
scale(-200, 100, 2, 2)
draw_circle(200, 100, 100, 'pink')
rotate(45)
draw_circle(-400, 100, 50, 'black')

turtle.done()
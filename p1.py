import turtle

def bresenham(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    xStep = 1 if x2 > x1 else -1
    yStep = 1 if y2 > y1 else -1
    error = 2 * dy - dx
    line_points = []
    x , y = x1, y1

    for _ in range(dx + 1):
        line_points.append((x, y))
        if error > 0:
            y += yStep
            dy = 2 * dx
        dx = 2 * dy
        x += xStep
    return line_points

x1, y1 = 50, 50
x2, y2 = 200, 200

line_points = bresenham(x1, y1, x2, y2)

for x, y in line_points:
    turtle.goto((x, y))

turtle.done()
import turtle

def sierpinski(points, degree, t):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    t.fillcolor(colormap[degree])
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    for point in points:
        t.goto(point[0], point[1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

    if degree > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])], degree-1, t)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])], degree-1, t)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])], degree-1, t)

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

t = turtle.Turtle()
my_points = [[-100, -50], [0, 100], [100, -50]]
sierpinski(my_points, 4, t)
turtle.done()
import turtle
import math

t = turtle.Turtle()

def skv(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.speed(10)

def go(r,color):
    x_point = 0
    y_point = -r
    skv(x_point,y_point)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
def pch(r,color):
    skv(0,0)
    t.pencolor(color)
    t.setheading(162)
    t.forward(r)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(math.cos(math.radians(18)) * 2 * r)
        t.right(144)
    t.end_fill()
    t.hideturtle()

if __name__ == "__main__":
    go(288,'crimson')
    go(234,'snow')
    go(174,'crimson')
    go(114,'blue')
    pch(114,'snow')
    turtle.done()
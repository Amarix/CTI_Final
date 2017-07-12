

import turtle
t=turtle.Turtle()
t.pensize(3)
t.setpos(0, 0)
t.speed(10)
counter = 0
r = 0.2
g = 0.05
b = 0.45
nOne = 0
nTwo = 6
color = (r, g, b)
def flake(d, a):
    for r in range(d):
        t.forward(d)
        t.left(a)
        d = d-1
    t.setpos(0, 0)
    t.left(60)
def getR(nOne, r):
    if nOne <= 5:
        r = round((r+0.1), 2)
    elif nOne >= 6:
        r = round((r-0.1),2)
    return (r)
def getG(nOne, g):
    if nOne <= 5:
        g = round((g+0.02), 2)
    elif nOne >= 6:
        g = round((g-0.02), 2)
    return (g)
def getB(nOne, b):
    if nOne <= 5:
        b = round((b+0.05), 2)
    elif nOne >= 6:
        b = round((b-0.05), 2)
    return (b)
while True:
    t.pencolor(color)
    if counter < 3:
        flake(30, 30)
    elif counter < 9:
        flake(60, 30)
    elif counter < 15:
        flake(80, 30)
    else:
        counter = 0
    counter = counter + 1
    if nOne <= 5:
        r = getR(nOne, r)
        g = getG(nOne, g)
        b = getB(nOne, b)
        color = (r, g, b)
        nOne = nOne+1
    elif nOne >= 6:
        r = getR(nOne, r)
        g = getG(nOne, g)
        b = getB(nOne, b)
        color = (r, g, b)
        nTwo = nTwo-1
        if nTwo <= 0:
            nOne = 0
            nTwo = 6

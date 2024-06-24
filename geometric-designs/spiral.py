from turtle import *
import random

def randomColorGenerator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def circularPage():
    speed(100)
    width(1)
    hideturtle()
    colormode(255)
    bgcolor("black")

    color = randomColorGenerator()
    
    for y in range(240):
        pencolor(color)
        circle(y)
        left(5)
        
circularPage()

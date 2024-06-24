from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(1)
hue=0.0

for i in range(150):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue += 0.005
    lt(40)
    circle(i)

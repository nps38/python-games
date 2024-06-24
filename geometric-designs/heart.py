from turtle import *
import math

def heartA(k):
    return 15*math.sin(k)**3
def heartB(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
speed(0)
bgcolor("black")
for i in range(500):
    goto(heartA(i)*20, heartB(i)*20)
    for j in range(5):
        color('#f73487')
    goto(0,0)
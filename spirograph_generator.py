"""
Spirograph Generator
"""
import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.colormode(255)
s.bgcolor('black')
t.speed(0)
t.pensize(2)
sizes = {'S': 50, 'M': 150, 'L': 250, 'XL': 450}

print('Hello! Welcome to the Spirograph Generator. Please select one of the following spirograph patterns: ')

def randomColorGenerator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
 
def square(size, colors):
    '''Create a square spirograph based with side lengths size'''
    for i in range(5):
        for color in colors:
            t.color(color)
            t.left(12)
            t.fd(size)
            t.left(90)
            t.fd(size)
            t.left(90)
            t.fd(size)
            t.left(90)
            t.fd(size)
            t.left(90)


def circle(size, colors):
    '''Create circle spirograph with radius size/2'''
    for i in range(6):
        for color in colors:
            t.color(color)
            t.circle(size/2)
            t.left(10)


def hexagon(size, colors):
    """Create a hexagonal swirl that repeates 'size' times """
    for i in range(size):
        t.pencolor(colors[i%6])
        t.width(i/101)
        t.fd(i)
        t.left(59)


def triangle(size, colors):
    '''Create a triangle spirograph based with side lengths size'''
    for i in range(5):
        for color in colors:
            t.color(color)
            t.left(12)
            t.fd(size)
            t.left(120)
            t.fd(size)
            t.left(120)
            t.fd(size)
            t.left(120)
 

def star(size, colors):
    """Create overlapping stars 'size'/100 times"""
    for i in range(int(size/100)):
        for color in colors:
            t.color(color)
            t.left(12)
            t.fd(size)
            t.left(150)
            t.fd(size)
            t.left(150)
            t.fd(size)
            t.left(150)
            t.fd(size)
            t.left(150)
 

def swirly(size, colors):
    """Create swirly of specified size"""
    for i in range(size):
        t.pencolor(colors[i%6])
        t.width(i/101)
        t.fd(i)
        t.left(40)


def squareSwirl(size, colors):
    """Create square swirly of specified size"""
    for i in range(size):
        t.pencolor(colors[i%6])
        t.forward(5+i)
        t.right(91)


def generateSpirograph():
    
    # Get shape input and size and make sure it is one of the possibilities
    shape = ''
    while (not(shape =='square' or shape =='circle' or shape =='hexagon' or shape =='triangle' or 
            shape =='star' or shape =='swirly' or shape =='squareSwirl')):
        shape = input('- square\n- circle\n- hexagon\n- triangle\n- star\n- swirly\n- squareSwirl\n') 
    
    #Getting size
    general_size = ''
    while (not(general_size == 'S' or general_size == 'M' or general_size == 'L' or general_size == 'XL')):
        general_size = input('Pick a size: S M L XL? ').upper()
        size = sizes[general_size]
        
    # Generate 6 random colors
    color1 = randomColorGenerator()
    color2 = randomColorGenerator()
    color3 = randomColorGenerator()
    color4 = randomColorGenerator()
    color5 = randomColorGenerator()
    color6 = randomColorGenerator()
    
    colors = [color1, color2, color3, color4, color5, color6]

    if shape == 'square':
        square(size, colors)
    elif shape == 'circle':
        circle(size, colors)
    elif shape == 'hexagon':
        hexagon(size, colors)
    elif shape == 'triangle':
        triangle(size, colors)
    elif shape == 'star':
        star(size, colors)
    elif shape == 'swirly':
        swirly(size, colors)
    elif shape == 'squareSwirl':
        squareSwirl(size, colors)

    playAgain = input("Do you want to play again? ").lower()
    if playAgain == 'yes':
        s.clear()
        # t = turtle.Turtle()
        # s = turtle.Screen()
        s.colormode(255)
        s.bgcolor('black')
        t.speed(0)
        t.pensize(2)
        generateSpirograph()
    else:
        s.exitonclick()
        
generateSpirograph()
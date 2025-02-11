import turtle as t
"""we first import turtle and set speed and hide the turtle for appropriate results"""

t.speed(30)
t.hideturtle()

def pole1(pole_color,length,width): #pole one
    t.penup()
    t.goto(-100,-150)
    t.pendown()
    t.left(90)
    t.fillcolor(pole_color)
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.end_fill()


def flag1(flag_color,length,width): # flag 1
    t.penup()
    t.goto(-100,200)
    t.pendown()
    t.fillcolor(flag_color)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.end_fill()


def circle_1(radius,circle_color): # circle of flag 1
    t.penup()
    t.goto(30,150)
    t.pendown()
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def pole2(pole_color,length,width): # pole 2
    t.penup()
    t.goto(150,-150)
    t.pendown()
    t.fillcolor(pole_color)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.end_fill()




def flag2(flag_color,length,width):  # flag 2
    t.penup()
    t.goto(150,100)
    t.pendown()
    t.fillcolor(flag_color)
    t.begin_fill()
    t.right(180)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length - 10)
    t.right(90)
    t.forward(width)
    t.end_fill()


def circle2(circle_color,radius):  # circle of flag 2
    t.penup()
    t.goto(260,50)
    t.pendown()
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def main():                  # calling all te functions from main and giving them values
    t.bgcolor('sky blue')
    pole1('black',350,10)
    flag1('red',200,100)
    circle_1(30,'white')
    pole2('black',250,10)
    flag2('red',150,100)
    circle2('white',30)
    input('enter any key to exit')
main()








from turtle import *


def red_circle_on():
    penup()
    goto(0, 100)
    pendown()
    color('red')
    begin_fill()
    circle(35)
    end_fill()

def red_circle_off():
    penup()
    goto(0, 100)
    pendown()
    color('red')
    circle(35)

def yellow_circle_on():
    penup()
    goto(0, 0)
    pendown()
    color('yellow')
    begin_fill()
    circle(35)
    end_fill()

def yellow_circle_off():
    penup()
    goto(0, 0)
    pendown()
    color('yellow')
    circle(35)

def green_circle_on():
    penup()
    goto(0, -100)
    pendown()
    color('green')
    begin_fill()
    circle(35)
    end_fill()

def green_circle_off():
    penup()
    goto(0, -100)
    pendown()
    color('green')
    circle(35)


question = input('Какой горит цвет, красный/жёлтый/зелёный?')
if question == 'красный':
    red_circle_on()
    yellow_circle_off()
    green_circle_off()

elif question == 'жёлтый':
    red_circle_off()
    yellow_circle_on()
    green_circle_off()
    
elif question == 'зелёный':
    red_circle_off()
    yellow_circle_off()
    green_circle_on()

exitonclick()
hideturtle()

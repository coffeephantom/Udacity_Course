#!/usr/bin/python
#-*- coding:utf-8 -*-

import turtle
def draw_circle(turtle,radius):
    turtle.circle(radius)
    
def draw_art():

    #initial the screen
    window=turtle.Screen()
    window.bgcolor("black")
    height=window.window_height()
    width=window.window_width()

    #initial the turtle
    oscar=turtle.Turtle()
    oscar.color("yellow")
    (x,y)=oscar.position()
    radius=10
    for x in xrange(1,5):
        for x in xrange(1,13):
            draw_circle(oscar, radius)
            oscar.left(30)
        radius=radius*2


    window.exitonclick()

draw_art()
    
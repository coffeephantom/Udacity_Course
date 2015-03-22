import turtle

def draw_square(turtle):
    for x in xrange(1,5):
        turtle.forward(100)
        turtle.right(90)
    
def draw_circle(turtle):
    turtle.circle(100)

def draw_triangle(turtle):
    turtle.forward(100)
    turtle.goto(50,50)  
    turtle.goto(0,0)

def draw_art():    
    window =turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle("turtle")
    brad.color("white")
    brad.fillcolor("yellow")
    brad.speed("fast")
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    draw_circle(angie)

    fred=turtle.Turtle()
    fred.shape("circle")
    fred.color("black")
    draw_triangle(fred)

    window.exitonclick()

draw_art()  
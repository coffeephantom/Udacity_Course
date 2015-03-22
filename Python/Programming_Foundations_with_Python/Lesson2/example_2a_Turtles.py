import turtle

def draw_square():
    brad = turtle.Turtle("turtle")
    brad.color("white")
    brad.fillcolor("yellow")
    brad.speed("fast")
    for x in xrange(1,5):
        brad.forward(100)
        brad.right(90)
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    fred=turtle.Turtle()
    fred.shape("circle")
    fred.color("black")
    fred.forward(100)
    fred.goto(50,50)  
    fred.goto(0,0)

def draw_art():    
    window =turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

draw_art()  
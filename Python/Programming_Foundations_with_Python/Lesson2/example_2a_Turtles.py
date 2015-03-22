import turtle

def draw_square():
    brad = turtle.Turtle("turtle")
    brad.color("white")
    brad.fillcolor("yellow")
    brad.speed("fast")
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

  
    
window =turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
window.exitonclick()  
import turtle

def draw_square(a_turtle) :
    for i in range(0,4):
        a_turtle.forward(100)
        a_turtle.left(123)
        #a_turtle.right(90)

def draw_art():
    window = turtle.Screen();
    window.bgcolor("blue")
    
    # create brad
    brad = turtle.Turtle();
    brad.speed(50)

    for i in range(0,37):
        draw_square(brad)
        brad.right(10)
    
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.sety(-100)
    angie.circle(100)

    window.exitonclick();

draw_art()

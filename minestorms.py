import turtle

def draw_square(some_turtle):
    for i in range(1,37):
        some_turtle.left(10)
        some_turtle.forward(10)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    #draw square
    cody = turtle.Turtle()
    cody.color("green")
    cody.shape("turtle")
    cody.speed(2)
    draw_square(cody)

    for i in range(1,37):
        draw_square(cody)
        cody.right(10)
        
    #draw circle
    #bob = turtle.Turtle()
    #bob.shape("turtle")
    #bob.circle(100)
    #bob.color("red")

    window.exitonclick()

draw_art()











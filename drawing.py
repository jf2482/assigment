import turtle
import random
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Star Pattern")

pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()
colors=["red","orange","yellow","green","cyan","blue","purple","pink"]

for i in range(40):
    pen.pencolor(random.choice(colors))
    side_length=40+(i*6)
    
    for _ in range(5):
        pen.forward(side_length)
        pen.right(144)

    pen.right(10)
    pen.pensize(1+i*0.1)

turtle.done()

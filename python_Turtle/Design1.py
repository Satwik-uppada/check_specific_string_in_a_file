import turtle
turtle.bgcolor("black")
s=turtle.Turtle()
s.speed(50)
s.pencolor("RED")
for i in range(400):
    s.forward(i)
    s.right(91)
turtle.hideturtle()
turtle.done()
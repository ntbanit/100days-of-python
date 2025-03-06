from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create a turtle object
square_turtle = Turtle()

def drawSquare(position, edgeSize): 
    square_turtle.penup()
    square_turtle.goto(position)
    square_turtle.pendown()
    square_turtle.color("white")
    square_turtle.fillcolor("white")
    square_turtle.begin_fill()
    for _ in range(4):
        square_turtle.forward(edgeSize)
        square_turtle.right(90)
    square_turtle.end_fill()

def drawSnake():
    length = 3
    pointSize = 20
    for i in range(length):
        drawSquare((i * pointSize, 0), pointSize)
drawSnake()
square_turtle.hideturtle()
screen.exitonclick()

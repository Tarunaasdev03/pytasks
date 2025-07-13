import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiling Emoji")

# Create turtle for the face
face = turtle.Turtle()
face.penup()
face.goto(0, -100)
face.pendown()
face.color("yellow")
face.begin_fill()
face.circle(100)
face.end_fill()

# Eyes
eyes = turtle.Turtle()
eyes.penup()
eyes.goto(-30, 30)
eyes.dot(20, "black")
eyes.goto(30, 30)
eyes.dot(20, "black")

# Smile
smile = turtle.Turtle()
smile.penup()
smile.goto(-40, -20)
smile.setheading(-60)
smile.pensize(5)
smile.pendown()
smile.circle(50, 120)

# Hide drawing turtles
face.hideturtle()
eyes.hideturtle()
smile.hideturtle()

# Keep the window open
turtle.done()


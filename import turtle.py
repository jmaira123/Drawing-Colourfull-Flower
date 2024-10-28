import turtle 

# Setup the turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)

#Define colors for the pattern
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet', 'white']

# loop to create the flower like pattern with overlapping circle
for i in range(12):
    t.pencolor(colors[i % len(colors)])
    for j in range(6):
        t.circle(100)
        t.left(60)
    t.left(30)

# hide the turtle and complete the drawing
t.hideturtle()
turtle.done()
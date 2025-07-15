import turtle

# Function to draw the tree
def tree(branchLen, t):
    if branchLen > 10:
        # Set color based on branch length
        if branchLen > 40:
            t.pencolor("brown")  # Thick branches
        else:
            t.pencolor("green")  # Leaves

        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)  # Right branch
        t.left(40)
        tree(branchLen - 15, t)  # Left branch
        t.right(20)
        t.backward(branchLen)  # Return to previous position

# Setup turtle screen and turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Background color
t.left(90)  # Point upwards
t.speed(0)  # Fastest drawing

# Draw the tree
tree(100, t)

# Finish
t.hideturtle()  # Hide turtle cursor
turtle.done()

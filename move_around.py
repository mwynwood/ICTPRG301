import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Move Around")
wn.bgcolor("green")
wn.setup(width=600, height=600)

# Player
player = turtle.Turtle()
player.shape("circle")
player.color("yellow")
# player.penup()
player.goto(0,0)
player.direction = "stop"

# Functions
def go_up():
    if player.direction != "down":
        player.direction = "up"

def go_down():
    if player.direction != "up":
        player.direction = "down"

def go_left():
    if player.direction != "right":
        player.direction = "left"

def go_right():
    if player.direction != "left":
        player.direction = "right"

def move():
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + 10)

    if player.direction == "down":
        y = player.ycor()
        player.sety(y - 10)

    if player.direction == "left":
        x = player.xcor()
        player.setx(x - 10)

    if player.direction == "right":
        x = player.xcor()
        player.setx(x + 10)

    player.direction = "stop"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the borders
    if player.xcor()>290:
        player.setx(290)
    if player.xcor()<-290:
        player.setx(-290)
    if player.ycor()>290:
        player.sety(290)
    if player.ycor()<-290:
        player.sety(-290)

    move()

wn.mainloop()
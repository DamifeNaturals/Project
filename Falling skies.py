import turtle
import random
import winsound

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling skies by Damilola @ 8 years old")
wn.bgcolor("green")
wn.bgpic("Background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("deerright.gif")
wn.register_shape("deerleft.gif")
wn.register_shape("nut.gif")
wn.register_shape("hunter.gif")

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("deerright.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create a list of good_guys
good_guys = []


# Add the good_guys
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("nut.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)

# Create a list of bad_guys
bad_guys = []


# Add the bad_guys
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("hunter.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = 0.5
    bad_guys.append(bad_guy)

# Add the pen
pen = turtle.Turtle()
pen.ht()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, -260)
font = ("Papyrus", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)


# Functions
def go_left():
    player.direction = "left"
    player.shape("deerleft.gif")


def go_right():
    player.direction = "right"
    player.shape("deerright.gif")


# Keyboard binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


running = True
# Main game loop
while running:

    # Update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # Move the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if of screen
        if y < -300:
            x = random.randint(-300, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # Check for player and good_guy collision
        if good_guy.distance(player) < 40:
            x = random.randint(-300, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
            winsound.PlaySound("power_up_01.ogg", winsound.SND_ASYNC)

        # Move the bad_guys
        for bad_guy in bad_guys:
            y = bad_guy.ycor()
            y -= bad_guy.speed
            bad_guy.sety(y)

        # Check if of screen
        if y < -300:
            x = random.randint(-300, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # Check for player and bad_guy collision
        if bad_guy.distance(player) < 10:
            x = random.randint(-300, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            lives -= 1
            score -= 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
            winsound.PlaySound("pingpong.mp3", winsound.SND_ASYNC)
        if lives < 1:
            running = False

wn.mainloop()

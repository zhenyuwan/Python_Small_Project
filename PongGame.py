import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by wan")
wn.bgcolor("black")
wn.setup(width=800, height=600) # size of the window
wn.tracer(0) # stop the window from updating

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of turtle module
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
# default size of turtle shape is 20 by 20, stretch_wid will make width 100
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1) 
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 # movement of ball in x-axis
ball.dy = 0.2 # movement of ball in y-axis

# Pen
player_A_score = 0
player_B_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    # return the y variable of turtle module
    # Set the paddle's position to go up by 20 pixel
    paddle_a.sety(paddle_a.ycor()+20) 

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor()-20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor()+20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor()-20)

def beep():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

# Keyboard Binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when press lowercase w on keyboard, call function paddle_a_up
wn.onkeypress(paddle_a_down, "s")    
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down") 

# Main game loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        beep()
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        beep()
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        beep()
        ball.setx(390)
        player_A_score += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(player_A_score,player_B_score), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -390:
        beep()
        ball.setx(-390)
        player_B_score += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(player_A_score,player_B_score), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    # Paddle and ball collision
    if paddle_a.xcor() - 20 < ball.xcor() and paddle_a.ycor() + 60 > ball.ycor() and paddle_a.xcor() + 20 > ball.xcor() and paddle_a.ycor() - 60 < ball.ycor():
        ball.dx *= -1
        ball.dy *= -1

    if paddle_b.xcor() - 20 < ball.xcor() and paddle_b.ycor() + 60 > ball.ycor() and paddle_b.xcor() + 20 > ball.xcor() and paddle_b.ycor() - 60 < ball.ycor():
        ball.dx *= -1
        ball.dy *= -1
    
     


#imported turtle module
import turtle

wind = turtle.Screen() #initialize screen
wind.title("ping pong by mohamed") #set the title of the window
wind.bgcolor("black") #set the background of the window 
wind.setup(width=800, height=600) #set the width and the height of the window
wind.tracer(0)  #stops the window from updating automatically

#madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=8, stretch_len=1)
madrab1.penup()
madrab1.goto(-350, 0)

#madrab2
madrab2 = turtle.Turtle() #intializes turtle object(shape)
madrab2.speed(0) #set the speed of the animation 
madrab2.shape("square") #set the shape of the objects
madrab2.color("red") #set the color of the shape
madrab2.shapesize(stretch_wid=8, stretch_len=1) #set the shape to meet the size
madrab2.penup() #stops the objects from drawing lines
madrab2.goto(350, 0) #set the position of the objects

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

#score
score1= 0
score2= 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: 0 player 2: 0", align="center" , font=("courier", 24,"normal"))

#functions
def madrab1_up():
    y = madrab1.ycor() #get the y coordinate of the madrab1
    y += 20 #set the y to increase by 20
    madrab1.sety(y) #set the y of the madrab1

#functions
def madrab1_down():
    y = madrab1.ycor()
    y -= 20 
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20 
    madrab2.sety(y)

#functions
def madrab2_down():
    y = madrab2.ycor()
    y -= 20 
    madrab2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
#main game loop
while True:
    wind.update() #update the screen everytime the loop runs

     #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--->+0.3 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--->+0.3 yaxis

    #border check, toop border +300px, bootom border -300px, ball is 20px
    if ball.ycor() >290: #if ball is at top border 
        ball.sety(290) #set y cordinate +290
        ball.dy *= -1 #reverse direction, making +0.3--->-0.3

    if ball.ycor() <-290: #if ball is at bottom border 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390: #if ball is at right border 
        ball.goto(0 , 0) #retunr ball to centre
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center" , font=("courier", 24,"normal"))
    
    if ball.xcor() <-390: #if ball is at left border
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center" , font=("courier", 24,"normal"))
     
     #tasadom madrab and ball 

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor()-40):
         ball.setx(340)
         ball.dx *= -1
    
    if (ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor()-40):
         ball.setx(-340)
         ball.dx *= -1
    


      
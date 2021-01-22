import turtle
import os
import time
# define the window
ScreenWidth=600
ScreenHeight=500
wn=turtle.Screen()
wn.bgcolor("Black")
wn.title("War Game")
wn.screensize(ScreenWidth,ScreenHeight)
wn.tracer(0)
#define the Border
Border_Pen=turtle.Turtle()
Border_Pen.speed(0)
Border_Pen.penup()
Border_Pen.setposition(-ScreenWidth/2,-ScreenHeight/2)
Border_Pen.pendown()
Border_Pen.pensize(3)
Border_Pen.color("yellow")
for i in range(2):
    Border_Pen.forward(ScreenWidth)
    Border_Pen.left(90)
    Border_Pen.forward(ScreenHeight)
    Border_Pen.left(90)
Border_Pen.hideturtle()
#define Player1
Player1= turtle.Turtle()
Player1.shape("square")
Player1.color("blue")
Player1.shapesize(1.5,1.5)
Player1.penup()
Player1.setposition(0,-ScreenHeight/2 + 20)
#define Player2
Player2= turtle.Turtle()
Player2.shape("square")
Player2.color("red")
Player2.shapesize(1.5,1.5)
Player2.penup()
Player2.setposition(0,ScreenHeight/2 -20)
#Moving functions
playersSpeed=30
def moveRightP1():
    x=Player1.xcor()
    Player1.setx(x+playersSpeed)
def moveLeftP1():
    x=Player1.xcor()
    Player1.setx(x-playersSpeed)
def moveRightP2():
    x=Player2.xcor()
    Player2.setx(x+playersSpeed)
def moveleftP2():
    x=Player2.xcor()
    Player2.setx(x-playersSpeed)
#shooting functions
def P1shoot():
    if len(P1Bullets)<3:
        P1createbullet(Player1.xcor(),Player1.ycor())
def P2shoot():
    if len(P2Bullets)<3:
        P2createbullet(Player2.xcor(),Player2.ycor())
#Collision Check function
def collision(bullet,player):
    distance=20
    if bullet.xcor() > player.xcor()-distance and bullet.xcor()<player.xcor()+distance:
        if bullet.ycor() >player.ycor()-distance and bullet.ycor()<player.ycor()+distance:
            return True
    return False
turtle.listen()
turtle.onkeypress(moveRightP1,"Right")
turtle.onkeypress(moveLeftP1,"Left")
turtle.onkeypress(moveRightP2,"d")
turtle.onkeypress(moveleftP2,"a")
turtle.onkeypress(P1shoot,"Up")
turtle.onkeypress(P2shoot,"space")
#Bullets
P1Bullets=[]
P2Bullets=[]
def P1createbullet(x,y):
    bullet= turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.shapesize(0.75)
    bullet.penup()
    bullet.setposition(x,y)
    P1Bullets.append(bullet)
def P2createbullet(x,y):
    bullet= turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.shapesize(0.75)
    bullet.penup()
    bullet.setposition(x,y)
    P2Bullets.append(bullet)

while True:
    gameover=False
    for i,bull in enumerate(P1Bullets):
        y=bull.ycor()
        if y>ScreenHeight:
            P1Bullets.pop(i)
        else:
            bull.sety(y+0.5)
            if collision(bull,Player2):
                gameover=True

    for i,bull in enumerate(P2Bullets):
        y=bull.ycor()
        if y<-ScreenHeight:
            P2Bullets.pop(i)
        else:
            bull.sety(y-0.5)
            if collision(bull,Player1):
                gameover=True
    if not gameover:
        wn.update()
    else:
        break
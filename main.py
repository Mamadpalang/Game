import turtle
import math
from Player import *
from func import *
from TurtleWindow import *
from Bullets import *
import os
import time
# define the window
ScreenWidth = 600
ScreenHeight=500
w=TurtleWindow(ScreenWidth,ScreenHeight,"war Game")
window=w.getWindow()
#define Player1
Player1=Player(0, -ScreenHeight/2 + 20, "Blue")
Player1.drawpipe(90)
#define Player2
Player2=Player(0, ScreenHeight/2 - 20, "Red")
Player2.drawpipe(270)
#Moving functions
playersSpeed=30
f = Func()
def moverightP1():
    f.hMove(Player1.getPlayer(), playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveLeftP1():
    f.hMove(Player1.getPlayer(), -playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveRightP2():
    f.hMove(Player2.getPlayer(), playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveleftP2():
    f.hMove(Player2.getPlayer(), -playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveUpP1():
    f.vMove(Player1.getPlayer(), playersSpeed, -ScreenHeight/2, 0)
def moveDownP1():
    f.vMove(Player1.getPlayer(), -playersSpeed, -ScreenHeight/2, ScreenHeight/2)
def moveUpP2():
    f.vMove(Player2.getPlayer(), playersSpeed, -ScreenHeight/2, ScreenHeight/2)
def moveDownP2():
    f.vMove(Player2.getPlayer(), -playersSpeed, 0, ScreenHeight/2)
#shooting functions
def P1shoot():
    f.shoot(Player1)
def P2shoot():
    f.shoot(Player2)
#Collision Check function
def collision(bullet,player):
    distance=20
    if bullet.xcor() > player.xcor()-distance and bullet.xcor()<player.xcor()+distance:
        if bullet.ycor() >player.ycor()-distance and bullet.ycor()<player.ycor()+distance:
            return True
    return False
turtle.listen()
turtle.onkeypress(moverightP1, "Right")
turtle.onkeypress(moveLeftP1, "Left")
turtle.onkeypress(moveUpP1, "Up")
turtle.onkeypress(moveDownP1, "Down")
turtle.onkeypress(P1shoot, "0")

turtle.onkeypress(moveRightP2,"d")
turtle.onkeypress(moveleftP2,"a")
turtle.onkeypress(moveUpP2,"w")
turtle.onkeypress(moveDownP2,"s")
turtle.onkeypress(P2shoot, "space")

while True:
    p1Angle = Player1.Pipe.heading()
    Player1.rotatepipe(0.2)
    p2Angle = Player2.Pipe.heading()
    Player2.rotatepipe(0.2)
    gameover= False
    for i, bull in enumerate(Player1.getMagazine()):
        y=bull.ycor()
        x=bull.xcor()
        if y > ScreenHeight/2 or y < -ScreenHeight/2 or x>ScreenWidth/2 or x < -ScreenWidth/2:
            bull.reset()
            Player1.removeBullet(i)
        else:
            bull.sety(y+1*math.sin(math.radians(bull.heading())))
            bull.setx(x+1*math.cos(math.radians(bull.heading())))
            if collision(bull, Player2.getPlayer()):
                gameover = True

    for i, bull in enumerate(Player2.getMagazine()):
        y=bull.ycor()
        x = bull.xcor()
        if y > ScreenHeight/2 or y < -ScreenHeight/2 or x>ScreenWidth/2 or x < -ScreenWidth/2:
            bull.reset()
            Player2.removeBullet(i)
        else:
            bull.sety(y + 1 * math.sin(math.radians(bull.heading())))
            bull.setx(x + 1 * math.cos(math.radians(bull.heading())))
            if collision(bull, Player1.getPlayer()):
                gameover = True
    if not gameover:
        window.update()
    else:
        break
d=input("Press any key to close")
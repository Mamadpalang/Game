import turtle
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
Player1=Player(0, -ScreenHeight/2 + 20, "Green")
#define Player2
Player2=Player(0, ScreenHeight/2 - 20, "Red")
#Moving functions
playersSpeed=30
f = Func()
def moverightP1():
    f.move(Player1.getPlayer(), playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveLeftP1():
    f.move(Player1.getPlayer(), -playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveRightP2():
    f.move(Player2.getPlayer(), playersSpeed, -ScreenWidth/2, ScreenWidth/2)
def moveleftP2():
    f.move(Player2.getPlayer(), -playersSpeed, -ScreenWidth/2, ScreenWidth/2)
#shooting functions
def P1shoot():
    if len(Player1.getMagazine()) < 3:
        b= Bullets(Player1.Pl.xcor(), Player1.Pl.ycor())
        Player1.addBullet(b.get())
def P2shoot():
    if len(Player2.getMagazine()) < 3:
        b = Bullets(Player2.Pl.xcor(), Player2.Pl.ycor())
        Player2.magazine.append(b.get())
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
turtle.onkeypress(moveRightP2,"d")
turtle.onkeypress(moveleftP2,"a")
turtle.onkeypress(P1shoot, "Up")
turtle.onkeypress(P2shoot, "space")

while True:
    gameover= False
    for i, bull in enumerate(Player1.getMagazine()):
        y=bull.ycor()
        if y > ScreenHeight:
            Player1.removeBullet(i)
        else:
            bull.sety(y+0.5)
            if collision(bull, Player2.getPlayer()):
                gameover = True

    for i, bull in enumerate(Player2.getMagazine()):
        y=bull.ycor()
        if y< -ScreenHeight:
            Player2.removeBullet(i)
        else:
            bull.sety(y-0.5)
            if collision(bull, Player1.getPlayer()):
                gameover = True
    if not gameover:
        window.update()
    else:
        break
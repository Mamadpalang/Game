import turtle
import math
from Player import *
from func import *
from TurtleWindow import *
from Bullets import *
import ctypes
import winsound
import os
import time
# define the window
p1score=0
p2score=0
while True:
    ScreenWidth = 600
    ScreenHeight=500
    w=TurtleWindow(ScreenWidth,ScreenHeight,"war Game")
    window=w.getWindow()
    #define Player1
    Player1=Player(0, -ScreenHeight/2 + 20, "Blue")
    Player1.drawpipe(90)
    Player1.writeScore(-ScreenWidth/2+20,ScreenHeight/2-40,p1score)
    #define Player2
    Player2=Player(0, ScreenHeight/2 - 20, "Red")
    Player2.drawpipe(270)
    Player2.writeScore(-ScreenWidth/2+20,ScreenHeight/2-70,p2score)
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
        Player1.shoot()
    def P2shoot():
        Player2.shoot()
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
        barrelSpeed = 0.2
        bulletSpeed=0.5
        p1Angle = Player1.Pipe.heading()
        Player1.rotatepipe(barrelSpeed)
        p2Angle = Player2.Pipe.heading()
        Player2.rotatepipe(barrelSpeed)
        gameover= "False"
        for i, (b,state) in enumerate(Player1.getMagazine()):
            bull=b.get()
            y = bull.ycor()
            x = bull.xcor()
            if state:
                if y > ScreenHeight/2 or y < -ScreenHeight/2 or x>ScreenWidth/2 or x < -ScreenWidth/2:
                    Player1.resetBullet(i)
                else:
                    bull.sety(y+bulletSpeed*math.sin(math.radians(bull.heading())))
                    bull.setx(x+bulletSpeed*math.cos(math.radians(bull.heading())))
                    if collision(bull, Player2.getPlayer()):
                        gameover = "Player1"

        for i, (b,state) in enumerate(Player2.getMagazine()):
            bull=b.get()
            y=bull.ycor()
            x = bull.xcor()
            if state:
                if y > ScreenHeight/2 or y < -ScreenHeight/2 or x>ScreenWidth/2 or x < -ScreenWidth/2:
                    Player2.resetBullet(i)
                else:
                    bull.sety(y + bulletSpeed * math.sin(math.radians(bull.heading())))
                    bull.setx(x + bulletSpeed * math.cos(math.radians(bull.heading())))
                    if collision(bull, Player1.getPlayer()):
                        gameover = "Player2"
        if gameover == "False":
            window.update()
        elif gameover == "Player1":
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            Player2.Pl.shape("turtle")
            window.update()
            p1score+=1
            break
        elif gameover == "Player2":
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            Player1.Pl.shape("turtle")
            window.update()
            p2score+=1
            break
    window.clear()
    result=ctypes.windll.user32.MessageBoxW(0, "Do you want to play again", "Game Over", 1)
    print(result)
    if result==2:
        break

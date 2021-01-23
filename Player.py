import turtle
import math
from Bullets import *
import winsound
class Player:
    Pl = turtle.Turtle()
    def __init__(self,x,y,color):
        self.magazine = []
        self.score=0
        self.Pl = turtle.Turtle()
        self.Pl.shape("square")
        self.color=color
        self.Pl.color(color)
        self.Pl.shapesize(1.5, 1.5)
        self.Pl.penup()
        self.Pl.setposition(x,y)
    def getPlayer(self):
        return self.Pl
    def writeScore(self,x,y,score):
        Score_Pen = turtle.Turtle()
        Score_Pen.speed(0)
        Score_Pen.color(self.color)
        Score_Pen.penup()
        Score_Pen.clear()
        Score_Pen.setposition(x, y)
        Score_Pen.write("Score : "+ str(score),align="left",font=("Arial",14,"normal"))
        Score_Pen.hideturtle()

#Magazine Bullet and shooting
    def getMagazine(self):
        return self.magazine
    def removeBullet(self, index):
        self.magazine.pop(index)
    def shoot(self):
        if len(self.magazine) < 3:
            winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)
            b = Bullets(self.Pl.xcor(), self.Pl.ycor(), self.Pipe.heading())
            self.magazine.append([b, True])
        else:
            for i in self.magazine:
                if not i[1]:
                    winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)
                    i[1] = True
                    i[0].setAngle(self.Pl.xcor(), self.Pl.ycor(), self.Pipe.heading())
                    i[0].show()
                    break
    def resetBullet(self,index):
        self.magazine[index][1] = False
        self.magazine[index][0].setAngle(self.Pl.xcor(), self.Pl.ycor(), -self.magazine[index][0].getAngle())
        self.magazine[index][0].hide()
#Barrel
    def drawpipe(self,angle):
        self.Pipe = turtle.Turtle()
        self.Pipe.shape("square")
        self.Pipe.color("Green")
        self.Pipe.shapesize(0.25, 1.5)
        self.Pipe.penup()
        self.Pipe.setposition(self.Pl.xcor()+(20*math.cos(math.radians(angle))), self.Pl.ycor()+(20*math.sin(math.radians(angle))))
        self.Pipe.left(angle)
    def removepipe(self):
        self.Pipe.reset()
    def getPipe(self):
        return  self.Pipe
    def rotatepipe(self,angle):
        self.Pipe.setposition(self.Pl.xcor() + (20 * math.cos(math.radians(self.Pipe.heading()))),self.Pl.ycor() + (20 * math.sin(math.radians(self.Pipe.heading()))))
        self.Pipe.left(angle)


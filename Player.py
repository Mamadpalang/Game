import turtle
import math
class Player:
    Pl = turtle.Turtle()
    def __init__(self,x,y,color):
        self.magazine = []
        self.Pl = turtle.Turtle()
        self.Pl.shape("square")
        self.Pl.color(color)
        self.Pl.shapesize(1.5, 1.5)
        self.Pl.penup()
        self.Pl.setposition(x,y)
    def getPlayer(self):
        return self.Pl

    def getMagazine(self):
        return self.magazine

    def addBullet(self, bullet):
        self.magazine.append(bullet)

    def removeBullet(self, index):
        self.magazine.pop(index)
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


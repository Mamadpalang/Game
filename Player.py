import  turtle
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


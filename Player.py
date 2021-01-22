import  turtle
class Player:
    def __init__(self,x,y,color):
        Player1 = turtle.Turtle()
        Player1.shape("square")
        Player1.color(color)
        Player1.shapesize(1.5, 1.5)
        Player1.penup()
        Player1.setposition(x,y)
    magazine=[]
    def getMagazine(self):
        return self.magazine
    def addBullet(self,bullet):
        self.magazine.append(bullet)
    def removeBullet(self,index):
        self.magazine.pop(index)


import turtle
class Bullets:
    bullet = turtle.Turtle()
    def __init__(self, x, y,angle):
        self.bullet = turtle.Turtle()
        self.bullet.shape("circle")
        self.bullet.color("yellow")
        self.bullet.shapesize(0.75)
        self.bullet.penup()
        self.bullet.left(angle)
        self.bullet.speed(0)
        self.bullet.setposition(x, y)
    def get(self):
        return self.bullet

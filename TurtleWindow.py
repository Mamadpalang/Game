import turtle
class TurtleWindow:
    def __init__(self,x,y,title):
        self.wn = turtle.Screen()
        self.wn.bgcolor("Black")
        self.wn.title("War Game")
        self.wn.screensize(x, y)
        self.wn.tracer(0)
        # define the Border
        Border_Pen = turtle.Turtle()
        Border_Pen.speed(0)
        Border_Pen.penup()
        Border_Pen.setposition(-x / 2, -y / 2)
        Border_Pen.pendown()
        Border_Pen.pensize(3)
        Border_Pen.color("yellow")
        for i in range(2):
            Border_Pen.forward(x)
            Border_Pen.left(90)
            Border_Pen.forward(y)
            Border_Pen.left(90)
        Border_Pen.hideturtle()

    def getWindow(self):
        return self.wn

from Bullets import *
import winsound
class Func:

    def __init__(self):
        return

    def hMove(self, Player1, playersSpeed, l_limit, r_limit):
        x = Player1.xcor()
        winsound.PlaySound("fastinvader1.wav", winsound.SND_ASYNC)
        if x + playersSpeed > l_limit and x+ playersSpeed <r_limit:
            Player1.setx(x + playersSpeed)
    def vMove(self, Player1, playersSpeed, b_limit, t_limit):
        y = Player1.ycor()
        winsound.PlaySound("fastinvader1.wav", winsound.SND_ASYNC)
        if y + playersSpeed >b_limit and y+ playersSpeed <t_limit:
            Player1.sety(y + playersSpeed)



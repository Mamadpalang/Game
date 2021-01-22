class Func:

    def __init__(self):
        return

    def move(self, Player1, playersSpeed, l_limit, r_limit):
        x = Player1.xcor()
        if x + playersSpeed > l_limit and x+ playersSpeed <r_limit:
            Player1.setx(x + playersSpeed)


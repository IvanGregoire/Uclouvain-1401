import turtle
from Robot import Robot  # Importer la classe Robot

class TurtleBot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.__t = turtle.Turtle()
        self.__wn = turtle.Screen()

    def wn(self):
        return self.__wn

    def bot(self):
        return self.__t

    def move_forward(self, distance):
        super().move_forward(distance)
        self.bot().forward(distance)

    def move_backward(self, distance):
        super().move_backward(distance)
        self.bot().backward(distance)

    def turn_left(self):
        super().turn_left()
        self.bot().left(90)

    def turn_right(self):
        super().turn_right()
        self.bot().right(90)

    def position(self):
        return self.bot().pos()

    def angle(self):
        return self.bot().heading()

    def __str__(self):
        return f"{self.name()}@{self.position()} angle: {self.angle()}"

    def wait(self):
        self.wn().mainloop()

    def unplay(self):
        super().unplay()

if __name__ == '__main__':

    
    """hagrid = TurtleBot("Hagrid sur sa moto magique")

    print(hagrid)

    hagrid.move_forward(50)
    hagrid.turn_left()
    print(hagrid)

    hagrid.move_forward(50)
    hagrid.turn_left()
    print(hagrid)

    hagrid.move_forward(50)
    hagrid.turn_left()
    print(hagrid)

    hagrid.move_forward(50)
    print(hagrid)

    hagrid.move_forward(50)
    hagrid.turn_right()
    print(hagrid)
    hagrid.move_forward(50)
    hagrid.turn_right()
    print(hagrid)
    hagrid.move_forward(50)
    hagrid.turn_right()
    print(hagrid)
    hagrid.move_forward(50)
    hagrid.turn_right()
    print(hagrid)
    print(hagrid.history())

    hagrid.unplay()

    print(hagrid.history())

    hagrid.wait()"""


from manim import *

class MovingAround(Scene):
    def construct(self):
        #creates a square of stadard size and the color blue
        square = Square(color=BLUE, fill_opacity=1)

        #shifts the quare to the left
        self.play(square.animate.shift(LEFT))
        #turns the quare orange
        self.play(square.animate.set_fill(ORANGE))
        #grow the square to 3 times its size
        self.play(square.animate.scale(3))
        #Rotate the square clockwise at a rate of 4
        self.play(square.animate.rotate(4))
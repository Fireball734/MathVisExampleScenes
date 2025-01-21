from manim import *

class MovingAround(Scene):
    def construct(self):
        #creates a square of stadard size and the color blue
        square = Square(color=BLUE, fill_opacity=1)

        #shifts the quare to the left
        self.play(square.animate.shift(LEFT))
        #turns the quare orange
        self.play(square.animate.set_fill(ORANGE))
        #shrink the square to 3/10 of its size
        self.play(square.animate.scale(0.3))
        #Rotate the square clockwise at a rate of 0.4
        self.play(square.animate.rotate(0.4))
from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        #create a circle that is 0.5 in radius and has the color 
        # blue
        circle = Circle(radius=0.5, color=PINK)
        #create a dot
        dot = Dot()
        #duplicate the dot and shift to to the right by 0.5
        dot2 = dot.copy().shift(RIGHT * 0.5)
        #make the dot show itself
        self.add(dot)
        
        #create a line that goes from the coordinates 1.5,0,0 to 
        # 2.5,0,0
        line = Line([1.5, 0, 0], [2.5, 0, 0])
        #make the line show itself
        self.add(line)

        #hello :)
        
        #make the circle appear by making it grow from the 
        # coordinates it lies on
        self.play(GrowFromCenter(circle))
        #move the dot from its original location to dot2's 
        # location
        self.play(Transform(dot, dot2))
        #move the dot along the path og the circle for 4 seconds 
        # at a linear rate
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        #rotate the dot about the point 1.5,0,0 so it perfectly 
        # touches both the line and circle in 1.5 seconds
        self.play(Rotating(dot, about_point=[1, 0, 0]), run_time=3)
        self.wait()
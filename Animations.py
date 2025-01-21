from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        #create a circle that is 1 in radius and has the color 
        # blue
        circle = Circle(radius=1, color=BLUE)
        #create a dot
        dot = Dot()
        #duplicate the dot
        dot2 = dot.copy().shift(RIGHT)
        #make the dot show itself
        self.add(dot)
        
        #create a line that goes from the coordinates 3,0,0 to 
        # 5,0,0
        line = Line([3, 0, 0], [5, 0, 0])
        #make the line show itself
        self.add(line)
        
        #make the circle appear by making it grow from the 
        # coordinates it lies on
        self.play(GrowFromCenter(circle))
        #move the dot from its original location to dot2's 
        # location
        self.play(Transform(dot, dot2))
        #move the dot along the path og the circle for 2 seconds 
        # at a linear rate
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        #rotate the dot about the point 2,0,0 so it perfectly 
        # touches both the line and circle in 1.5 seconds
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()
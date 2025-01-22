from manim import *

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        #creates a value tracker to track the value of the angle theta
        theta_tracker = ValueTracker(110)
        #create stationary line to serve as one half of an angle
        line1 = Line(LEFT, RIGHT)
        #create an adjustable line to serve as the other half of an angle
        line_moving = Line(LEFT, RIGHT)
        #clone the moving line to use as a reference
        line_ref = line_moving.copy()
        #method to rotate the moving line a certain number of degrees
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        #move the theta symbol so that it isn't overlapping the angle
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        #actually add the objects and make them visible
        self.add(line1, line_moving, a, tex)
        self.wait()
        #update the movin line's angle
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        #update the display of the angle
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )
        #create the initial angle at 40 degrees
        self.play(theta_tracker.animate.set_value(40))
        #increase the angle by 140 degrees
        self.play(theta_tracker.animate.increment_value(140))
        #change the color of theta to red in 0.5 seconds
        self.play(tex.animate.set_color(RED), run_time=0.5)
        #change the angle to precisely 350 degrees
        self.play(theta_tracker.animate.set_value(350))
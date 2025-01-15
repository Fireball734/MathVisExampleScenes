from manim import *
import numpy as np
import math

class AnimatingMethods(Scene):
    def construct(self):
        # Create a grid of Pi symbols
        grid = VGroup(*[
            MathTex(r"\pi") for _ in range(100)
        ]).arrange_in_grid(rows=10, cols=10, buff=0.1).scale_to_fit_height(4)
        
        self.add(grid)

        # Animate shifting the grid to the left
        self.play(grid.animate.shift(LEFT))

        # Animate shifting the grid to the left using an alternative syntax
        self.play(grid.animate.apply_function(lambda p: [p[0] - 1, p[1], p[2]]))

        # Set color of the grid to yellow
        self.play(grid.animate.set_color(YELLOW))
        self.wait()

        # Set a gradient color from blue to green
        self.play(grid.animate.set_color_by_gradient(BLUE, GREEN))
        self.wait()

        # Adjust the height of the grid
        self.play(grid.animate.scale_to_fit_height(TAU - DEFAULT_MOBJECT_TO_EDGE_BUFFER))
        self.wait()

        # Apply a complex function to transform the grid
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # Apply a general R^3 to R^3 function
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()

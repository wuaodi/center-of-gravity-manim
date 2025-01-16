from manim import *

class PlaneAngleOfAttack(Scene):
    def construct(self):
        # Load the airplane image and scale it
        plane = ImageMobject("plane.jpg").scale(0.4)
        
        # Initial position (on the right side of the screen)
        plane.move_to(RIGHT * 4)
        
        # Title for the scene
        title = Text("重心的应用", font_size=48).to_edge(UP)
        
        # Add the title to the scene
        self.play(Write(title))
        
        # Introduce the airplane image
        self.play(FadeIn(plane))
        
        # Simulate the change in angle of attack (moving left and changing angle)
        self.play(
            plane.animate.move_to(ORIGIN).rotate(-20 * DEGREES),  # Move left and increase angle of attack
            run_time=3
        )

        # Calculate the center of mass position
        center_of_mass = plane.get_center()

        # Add arrows and text to represent lift and weight
        weight_arrow = Arrow(start=center_of_mass + LEFT * 0.5, end=center_of_mass+ LEFT * 0.5 + DOWN * 2, color=BLUE)
        lift_arrow = Arrow(start=center_of_mass  + DOWN * 0.5, end=center_of_mass + UP * 2, color=GREEN)
        
        weight_label = Text("重力", font_size=24).next_to(weight_arrow, LEFT)
        lift_label = Text("升力", font_size=24).next_to(lift_arrow, UP)

        # Display the arrows and labels
        self.play(FadeIn(weight_arrow, lift_arrow, weight_label, lift_label))

        # Pause to show the forces
        self.wait(5)

        # Fade out the arrows and labels
        self.play(FadeOut(weight_arrow), FadeOut(lift_arrow), FadeOut(weight_label), FadeOut(lift_label))

        # Simulate the recovery of angle of attack (moving further left and decreasing angle)
        self.play(
            plane.animate.move_to(LEFT * 4).rotate(20 * DEGREES),  # Continue left and decrease angle of attack
            run_time=3
        )
        
        # Hold the final state for a moment
        self.wait(2)
        
        # End the animation by fading out all components
        self.play(FadeOut(plane), FadeOut(title))
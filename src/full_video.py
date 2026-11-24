"""
Full Video Runner for Linear Transformations.
Combines all 6 scenes into a single continuous, seamless presentation:
- Scene 1: Hook & Introduction (0:00 - 0:35)
- Scene 2: Understanding the Concept (0:35 - 1:20)
- Scene 3: Visual Intuition (1:20 - 2:20)
- Scene 4: Step-by-Step Worked Example (2:20 - 3:45)
- Scene 5: Geometric Interpretation (3:45 - 4:35)
- Scene 6: Summary & Credits (4:35 - 5:10)
"""

from manim import *
from src.scene1_hook import Scene1Hook
from src.scene2_concept import Scene2Concept
from src.scene3_visual_intuition import Scene3VisualIntuition
from src.scene4_worked_example import Scene4WorkedExample
from src.scene5_geometric_interpretation import Scene5GeometricInterpretation
from src.scene6_summary import Scene6Summary


class FullLinearTransformationsVideo(Scene):
    def construct(self):
        # Scene 1: Hook and Introduction
        Scene1Hook.construct(self)
        self.wait(0.5)

        # Scene 2: Understanding the Concept
        Scene2Concept.construct(self)
        self.wait(0.5)

        # Scene 3: Visual Intuition
        Scene3VisualIntuition.construct(self)
        self.wait(0.5)

        # Scene 4: Step-by-Step Worked Example
        Scene4WorkedExample.construct(self)
        self.wait(0.5)

        # Scene 5: Geometric Interpretation
        Scene5GeometricInterpretation.construct(self)
        self.wait(0.5)

        # Scene 6: Summary and Credits
        Scene6Summary.construct(self)

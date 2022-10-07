from Lab3_shape_classes import Circle, Rectangle
import matplotlib.pyplot as plt

class Draw:
    """Draws circles and rectangles in a cooridnate system"""
    def __init__(self, *shapes) -> None:
        self.shapes = shapes
    
    def draw(self) -> None:
        fig, ax = plt.subplots()
        ax.set(xlabel = "x", ylabel = "y", title = "Shape", xlim = (-5,5), ylim = (-5,5))

        for shape in self.shapes:
            if isinstance(shape, Circle):
                patch = plt.Circle((shape.x_center, shape.y_center), shape.radius, fill = False)
            elif isinstance(shape, Rectangle):
                patch = plt.Rectangle((shape.x_center, shape.y_center), shape.side_a, shape.side_b, fill = False)
    
            ax.add_patch(patch)
        plt.show()
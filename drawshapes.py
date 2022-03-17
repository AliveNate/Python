
# Turtle actually opens a black white screen and draws based on function instructions.
import turtle  # Library to help draw the shapes.

class Polygon:      # ex. triangles, squares, etc...
    def __init__(self, sides, name, size, color="red", line_thickness=2):     # What is important to a polygon
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color                              # default=red but can change when you create any shape
        self.line_thickness = line_thickness            # default=2 but can change when you create any shape
        self.interior_angles = (self.sides - 2) * 180   # Sum of interior angles = (sides - 2)*180
        self.angle = self.interior_angles / self.sides  # Each angle = ((sides - 2) * 180) / sides
    # -----------------------------
    """
    # Base Turtle Class method to draw a shape. 
    # We are not using this 'drawSquare'
    # This function turns 90degrees, so really only does a square.
    def drawSquare(self):               # pass in self, to access attributes
        for i in range(self.sides):     # square = 4 sides
            turtle.forward(100)         # forward 100 pixels
            turtle.right(90)            # turn right 90 degrees
                                        # loop 4 times for square.
        turtle.done
    """
    # -------------------------
    # More advanced draw function to draw any polygon
    # We included in our self.attributes above, the formula for polygon angles, so now we can draw any polygon.
    def drawPolygon(self):
        for i in range(self.sides):
            turtle.color(self.color)                # line color when we draw the shape
            turtle.pensize(self.line_thickness)     # how thick the line will be
            turtle.forward(100)                     # forward 100 pixels
            turtle.right(180 - self.angle)          # turn right degrees based on # of sides, and angle formula above
        """class Square inherits drawPolygon, so we can't have 'turtle.done()' here, or it will conflict if we draw a square"""
        #turtle.done()
    # -------------------------
# Inheritance and subclassing
# This is a class, that has 4 sides, + name Square, + inherits other polygon attributes.
class Square(Polygon):
    # We know a square will have 4 sides, and is named "Square" so we only have to pass in the other params
    def __init__(self, size=100, color="green", line_thickness=3):  # Original Polygon attributes
        # Use Polygon but square will always have 4 sides, and be named "Square" + entries.
        super().__init__(4, "Square", size, color, line_thickness)  # Pulls in 4 attributes, but adjusts sides and name.
    # ----------------------------------------
    # Copy the original drawPolygon function
    def drawPolygon(self):
        turtle.begin_fill()         # Extra method to start the fill
        super().drawPolygon()       # Copy the original drawPolygon methods.
        turtle.end_fill()           # Finish the shape fill in

# ------------------------
# ------------------------
# This is a class, that has 4 sides, + name Square, + inherits other polygon attributes.
# subclass
square = Square()    # Create square, with default polygon + default square(sides, name)
print(f"square.sides = {square.sides}")
print(f'square.angle = {square.angle}')
print(f'square.name  = {square.name}')
print(f'square.interior_angles = {square.interior_angles}')
print(f'------------------')
# ------------------------
# ------------------------
# Draw
#
# We created a simple turtle-hexagon function just for demonstration.
#       Once we used the polygon formula, the drawPolygon will draw any.
#       def __init__(self, sides, name, size, color="red", line_thickness=2):
hexagon = Polygon(6,  "Hexagon", 1000, "blue",  10)  # default color is red, but we can override that upon creation
#hexagon.drawPolygon()
# --------------------
square.drawPolygon()   # There was conflict drawing this, and drawing another above(hexagon)
#       If you look in the original 'drawPolygon' function, there is already a 'turtle.done()'
#       But since the 'Square' is an inherited class, we have to use 'turtle.done()' outside.
turtle.done()
import turtle

class Polygon:
	"""This is the documentation for the Polygon Class.
	Yaay!!!! I figured it out!"""
	
	def __init__(self, sides, name, size=100, color = "black", line_thickness = 5):
		self.sides = sides
		self.name = name
		self.size = size
		self.color = color
		self.line_thickness = line_thickness
		self.sum_of_angles = (self.sides-2) * 180
		self.interior_angle = self.sum_of_angles/self.sides
		self.exterior_angle = 180-self.interior_angle

	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.line_thickness)
		for i in range(self.sides):
			turtle.forward(self.size)
			turtle.right(self.exterior_angle)
		


# Inheritance

class Square(Polygon):
	def __init__(self, size = 100, color = 'blue', line_thickness = 20):
		super().__init__(4, "Square", size, color, line_thickness)

	def draw(self):
		turtle.begin_fill()
		super().draw()
		turtle.end_fill()





# square = Polygon(4, "Square", 100)
pentagon = Polygon(5, "Pentagon", 100)
hexagon = Polygon(6,"Hexagon", color = "blue")

# print(square.name, square.sides)
print(pentagon.name, pentagon.sides)
print(pentagon.__doc__)
# pentagon.draw()
# hexagon.draw()
square = Square()
square.draw()
turtle.done()




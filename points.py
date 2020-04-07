import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def plot(self):
		plt.scatter(self.x, self.y)
		plt.show()

point1 = Point(1,2)
print(point1.x)
print(point1.y)
print(point1.__doc__)
point1.plot()

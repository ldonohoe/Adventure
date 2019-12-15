# Created 6/19/19 by Liam Donohoe

# Keeps track of movement of sprites and follows accordingly
class Camera():
	
	def __init__(self):
		self.x = 250
		self.y = 250

	def setCam(self, x, y):
		self.x = x
		self.y = y

	def getCam(self):
		return (self.x, self.y)
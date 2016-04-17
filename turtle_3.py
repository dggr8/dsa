# Each of the command classes below hold information for one of the types of
# commands found in a graphics file. For each command there must be a draw
# method that is given a turtle and uses the turtle to draw the object.
import turtle

class GoToCommand:
	"""Here is the constructor defined with default values for width & color"""
	def __init__(self, x, y, width=1, color="black"):
		self.x = x
		self.y = y
		self.color = color
		self.width = width

	def draw(self,turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.goto(self.x,self.y)

class CircleCommand:
	def __init__(self, radius, width=1,color="black"):
		self.radius = radius
		self.width = width
		self.color = color

	def draw(self,turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.circle(self.radius)
		
class BeginFillCommand:
	def __init__(self, color):
		self.color = color

	def draw(self,turtle):
		turtle.fillcolor(self.color)
		turtle.begin_fill()

class EndFillCommand:
	def __init__(self):
		pass

	def draw(self,turtle):
		turtle.end_fill()

class PenUpCommand:
	def __init__(self):
		pass

	def draw(self,turtle):
		turtle.penup()

class PenDownCommand:
	def __init__(self):
		pass
	def draw(self,turtle):
		turtle.pendown()

class PyList:
	def __init__(self):
		self.items = []

	def append(self,item):
		self.items = self.items + [item]

	# define a special method called __iter__(self)
	def __iter__(self):
		for c in self.items:
			yield c

def main():
	filename = input("Please enter drawing filename: ")

	t = turtle.Turtle()
	screen = t.getscreen()
	file = open(filename,"r")

	# Create a PyList to hold the graphics commands that are read from file
	graphicsCommands = PyList()

	command = file.readline().strip()

	while command != "":
		
		if command=="goto":
			x = float(file.readline())
			y = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			cmd = GoToCommand(x,y,width,color)

		elif command=="circle":
			radius = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			cmd = CircleCommand(radius,width,color)

		elif command=="beginfill":
			color = file.readline().strip()
			cmd = BeginFillCommand(color)

		elif command=="endfill":
			cmd = EndFillCommand()

		elif command=="penup":
			cmd = PenUpCommand()

		elif command=="pendown":
			cmd = PenDownCommand()

		else:
			# Raise RuntimeError exception for this case
			raise RuntimeError("Unknown Command: "+ command)

		# Finish processing the record by adding the command to the sequence.
		graphicsCommands.append(cmd)

		# Read one more line to set up for the next time through the loop.
		command = file.readline().strip()

	for cmd in graphicsCommands:
		cmd.draw(t)

	file.close()
	t.ht()
	screen.exitonclick()
	print("Program Execution Completed.")

if __name__=="__main__":
	main()
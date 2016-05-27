class Hashset:
	def __init__(self,contents=[]):
		self.items = [None]*10
		self.numItems = 0

		for item in contents:
			self.add(item)

	
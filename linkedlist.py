class LinkedList:

	class __Node:
		def __init__(self,item,next=None):
			self.item = item
			self.next = next

		def getItem(self):
			return self.item

		def getNext(self):
			return self.next

		def setItem(self,item):
			self.item = item

		def setNext(self,next):
			self.next = next

	def __init__(self,contents=[]):
		self.first = LinkedList.__Node(None,None)
		self.last = self.first
		self.numItems = 0

		for e in contents:
			self.append(e)

	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			cursor = self.first.getNext()
			for i in range(index):
				cursor = cursor.getNext()


			return cursor.getItem()

		raise IndexError("LinkedList index out of range")

	def __setitem__(self,index,val):
		if index >= 0 and index < self.numItems:
			cursor= self.first.getNext()
			for i in range(index):
				cursor = cursor.getNext()

			cursor.setItem(val)
			return
		raise IndexError("LinkedList assignment index out of range")

	def __add__(self,other):
		if type(self) != type(other):
			raise TypeError("Concatenate undefined for "+\
				str(type(self)) + " + "+ str(type(other)))

		result = LinkedList()

		cursor = self.first.getNext()

		while cursor!=None:
			result.append(cursor.getItem())
			cursor = cursor.getNext()

		cursor = other.first.getNext()

		while cursor!=None:
			result.append(cursor.getItem())
			cursor = cursor.getNext()

		return result

	def append(self,item):
		node = LinkedList.__Node(item)
		self.last.setNext(node)
		self.last = node
		self.numItems += 1

	def insert(self,index,item):
		cursor = self.first

		if index < self.numItems:
			for i in range(index):
				cursor = cursor.getNext()

			node = LinkedList.__Node(item,cursor.getNext())
			cursor.setNext(node)
			self.numItems += 1
		else:
			self.append(item)

	def print_list(self):
		cursor = self.first.getNext()
		while cursor != None:
			print(cursor.item)
			cursor = cursor.getNext()

	def delete(self,index):
		cursor = self.first
		for i in range(index):
			cursor = cursor.getNext()

		cursor.setNext(cursor.getNext().getNext())

	def length(self):
		return self.numItems

	def __eq__(self,other):
		node1 = self.first
		node2 = other.first
		for i in range(self.numItems):
			node1 = node1.getNext()
			node2 = node2.getNext()
			if node1.item!=node2.item:
				return False

		return True

	def __contains__(self,item):
		cursor = self.first
		for i in range(self.numItems):
			cursor = cursor.getNext()
			if item==cursor.item:
				return True

		return False

	def __iter__(self):
		cursor = self.first
		for i in range(self.numItems):
			cursor = cursor.getNext()
			yield cursor.item

s = LinkedList()
s.append(2)
s.append(3)
s1 = LinkedList()
s1.append(2)
s1.append(3)

print(2 in s)
import copy
class Stack:
	def __init__(self):
		self.items = []

	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to pop an empty stack")

		topIdx = len(self.items) -1
		item = self.items[topIdx]
		del self.items[topIdx]
		return item

	def push(self,item):
		self.items.append(item)

	def top(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to get top of empty stack")

		topIdx = len(self.items) - 1
		return self.items[topIdx]

	def isEmpty(self):
		return len(self.items)==0

	def __len__(self):
		return len(self.items)

	def __contains__(self,item):
		return (item in self.items)

	def getList(self):
		return copy.deepcopy(self.items)

def main():
	s = Stack()
	lst = list(range(10))
	lst2 = []

	for k in lst:
		s.push(k)

	if s.top() == 9:
		print("Test 1 Passed")
	else:
		print("Test 1 Failed")

	while not s.isEmpty():
		lst2.append(s.pop())

	lst2.reverse()

	if lst2 != lst:
		print("Test 2 Failed")
	else:
		print("Test 2 Passed")

	try:
		s.pop()
		print("Test 3 Failed")
	except RuntimeError:
		print("Test 3 Passed")
	except:
		print("Test 3 Failed")
	
	try:
		s.top()
		print("Test 4 Failed")
	except RuntimeError:
		print("Test 4 Passed")
	except:
		print("Test 4 Failed")

if __name__ == '__main__':
	main()

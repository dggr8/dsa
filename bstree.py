class BinarySearchTree:
	#This is a Node class that is internal to the Binary Search Tree class
	class __Node:
		def __init__(self,val,left=None,right=None):
			self.val = val
			self.left = left
			self.right = right

		def getVal(self):
			return self.val

		def setVal(self,newval):
			self.val = newval

		def getLeft(self):
			return self.left

		def getRight(self):
			return self.right

		def setLeft(self,newleft):
			self.left = newleft

		def setRight(self,newright):
			self.right = newright

		def __iter__(self):
			if self.left != None:
				for elem in self.left:
					yield elem

			yield self.val

			if self.right != None:
				for elem in self.right:
					yield elem

		def trace(self):
			if self.getLeft() != None and self.getRight() != None:
				print(str(self.getVal())+" -> "+str(self.getLeft().getVal())+" & "+str(self.getRight().getVal()))
				self.getLeft().trace()
				self.getRight().trace()
			elif self.getLeft() != None:
				print(str(self.getVal())+" -> "+str(self.getLeft().getVal())+" & None")
				self.getLeft().trace()
			elif self.getRight() != None:
				print(str(self.getVal())+" -> None & "+str(self.getRight().getVal()))
				self.getRight().trace()
			else:
				print(str(self.getVal())+" only")

	def __init__(self):
		self.root = None

	def insert(self,val):

		def __insert(root,val):
			if root==None:
				return BinarySearchTree.__Node(val)

			if val < root.getVal():
				root.setLeft(__insert(root.getLeft(),val))
			else:
				root.setRight(__insert(root.getRight(),val))

			return root

		self.root = __insert(self.root,val)

	def __iter__(self):
		if self.root != None:
			return self.root.__iter__()
		else:
			return [].__iter__()
	
	def remove(self,item):
		node = self.root
		prev = None
		left = 0
		while node != None:
			if item < node.getVal():
				prev = node
				left = 1
				node = node.getLeft()
			elif item > node.getVal():
				prev = node
				left = 0
				node = node.getRight()
			else:
				break
		if node == None:
			return False
		if node.getLeft()==None and node.getRight()==None:
			if prev == None:
				self.root = None
			else:
				if left==1:
					prev.setLeft(None)
				else:
					prev.setRight(None)

		elif node.getLeft()==None:
			if prev == None:
				self.root = node.getRight()
			else:
				if left==1:
					prev.setLeft(node.getRight())
				else:
					prev.setRight(node.getRight())

		elif node.getRight()==None:
			if prev == None:
				self.root = node.getLeft()
			else:
				if left==1:
					prev.setLeft(node.getLeft())
				else:
					prev.setRight(node.getLeft())


			node = node.getLeft()
		else:
			replace = node.getLeft()
			if replace.getLeft()==None and replace.getRight()==None:
				node.setLeft(None)
				node.setVal(replace.getVal())
				return True
			prev = node
			while replace.getRight() != None:
				prev = replace
				replace = replace.getRight()

			node.setVal(replace.getVal())
			if replace.getLeft() != None:
				prev.setRight(replace.getLeft())
			else:
				prev.setRight(None)

		return True

def main():
	#s = input("Enter a list of numbers: ")
	s = "3 4 2 2.5 1 6 903 23 54"
	lst = s.split()

	tree = BinarySearchTree()

	for x in lst:
		tree.insert(float(x))

	for x in tree:
		print(x)

	tree.root.trace()
	while True:
		s = input("Enter a number to delete: ")
		if tree.remove(float(s)):
			print("Successfully removed")
		else:
			print("Couldn't remove")
		tree.root.trace()

if __name__ == "__main__":
	main()

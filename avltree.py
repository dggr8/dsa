class AVLTree:
	#This is a Node class that is internal to the AVLTree class
	class __Node:
		def __init__(self,val,parent=None,left=None,right=None):
			self.val = val
			self.parent = parent
			self.left = left
			self.right = right
			self.balance = 0

		def getVal(self):
			return self.val

		def setVal(self,newval):
			self.val = newval

		def getParent(self):
			return self.parent

		def setParent(self,newParent):
			self.parent = newParent

		def getBalance(self):
			return self.balance

		def setBalance(self,newBalance):
			self.balance = newBalance

		def getLeft(self):
			return self.left

		def getRight(self):
			return self.right

		def setLeft(self,newleft):
			self.left = newleft

		def setRight(self,newright):
			self.right = newright

		#def __eq__(self,other):
		#	if other==None:
		#		#Comparing a node with None gives error. So plotting an escape here.
		#		return False
		#	if self.val == other.val and self.left==other.left and self.right==other.right and self.parent==other.parent:
		#		return True
		#	else:
		#		return False

		def isLeft(self):
			if self.getParent()==None:
				return False
			if self.getParent().getLeft() == self:
				return True
			else:
				return False

		def isRight(self):
			if self.getParent()==None:
				return False
			if self.getParent().getRight() == self:
				return True
			else:
				return False

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
				print(str(self.getVal())+" -> "+str(self.getLeft().getVal())+" & "+str(self.getRight().getVal())+" Balance :"+str(self.getBalance())+" Parent :"+str(self.getBalance()))
				self.getLeft().trace()
				self.getRight().trace()
			elif self.getLeft() != None:
				print(str(self.getVal())+" -> "+str(self.getLeft().getVal())+" & None"+" Balance :"+str(self.getBalance())+" Parent : "+str(self.getParent().getVal()))
				self.getLeft().trace()
			elif self.getRight() != None:
				print(str(self.getVal())+" -> None & "+str(self.getRight().getVal())+" Balance :"+str(self.getBalance())+" Parent : "+str(self.getParent().getVal()))
				self.getRight().trace()
			else:
				print(str(self.getVal())+" only"+" Balance :"+str(self.getBalance())+" Parent : "+str(self.getParent().getVal()))

	def __init__(self):
		self.root = None

	def update_balance(self,node):
		if node.getBalance() > 1 or node.getBalance() < -1:
			self.rebalance(node)
			return
		
		if node.getParent() != None:
			print "Updating balance for %d" %node.getParent().getVal()
			print "Info: Node %d is " %node.getVal()
			if node.isRight():
				print "from %d"%node.getParent().getBalance()
				node.getParent().setBalance(node.getParent().getBalance()+1)
				print "to %d"%node.getParent().getBalance()
			elif node.isLeft():
				print "from %d"%node.getParent().getBalance()
				node.getParent().setBalance(node.getParent().getBalance()-1)
				print "to %d"%node.getParent().getBalance()

			if node.getParent().getBalance() != 0:
				self.update_balance(node.getParent())

	def rotateLeft(self,rotRoot):
		newRoot = rotRoot.getRight()
		rotRoot.setRight(newRoot.getLeft())
		if newRoot.getLeft()!= None:
			newRoot.getLeft().setParent(rotRoot)
		newRoot.setParent(rotRoot.getParent())
		if rotRoot == self.root:
			self.root = newRoot
		else:
			if rotRoot.isLeft():
				rotRoot.getParent().setLeft(newRoot)
			else:
				rotRoot.getParent().setRight(newRoot)
		newRoot.setLeft(rotRoot)
		rotRoot.setParent(newRoot)
		rotRoot.setBalance(rotRoot.getBalance() + 1 - min(newRoot.getBalance(),0))
		newRoot.setBalance(newRoot.getBalance() + 1 + max(rotRoot.getBalance(),0))

	def rotateRight(self,rotRoot):
		newRoot = rotRoot.getLeft()
		rotRoot.setLeft(newRoot.getRight())
		if newRoot.getRight() != None:
			newRoot.getRight().setParent(rotRoot)
		newRoot.setParent(rotRoot.getParent())
		if rotRoot == self.root:
			self.root = newRoot
		else:
			if rotRoot.isLeft():
				rotRoot.getParent().setLeft(newRoot)
			else:
				rotRoot.getParent().setRight(newRoot)
		newRoot.setRight(rotRoot)
		rotRoot.setParent(newRoot)
		rotRoot.setBalance(rotRoot.getBalance() + 2 - min(0,newRoot.getBalance()))
		newRoot.setBalance(newRoot.getBalance() + 1 + max(1,rotRoot.getBalance()))

	def rebalance(self,node):
		if node.getBalance() > 0:
			if node.getRight().getBalance() < 0:
				self.rotateRight(node.getRight())
				self.rotateLeft(node)
			else:
				self.rotateLeft(node)
		elif node.getBalance() < 0:
			if node.getLeft().getBalance() > 0:
				self.rotateLeft(node.getLeft())
				self.rotateRight(node)
			else:
				self.rotateRight(node)

	def insert(self,val):

		def __insert(root,val,parent=None):
			if root==None:
				new_node = AVLTree.__Node(val,parent,None,None)
				if parent != None:
					if val > parent.getVal():
						parent.setRight(new_node)
					else:
						parent.setLeft(new_node)
					self.update_balance(new_node)
				return new_node

			if val < root.getVal():
				root.setLeft(__insert(root.getLeft(),val,root))
			else:
				root.setRight(__insert(root.getRight(),val,root))

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
			if node.getParent() == None:
				self.root = None
			else:
				if left==1:
					node.getParent().setLeft(None)
				else:
					node.getParent().setRight(None)

		elif node.getLeft()==None:
			if node.getParent() == None:
				self.root = node.getRight()
			else:
				if left==1:
					node.getParent().setLeft(node.getRight())
				else:
					node.getParent().setRight(node.getRight())

		elif node.getRight()==None:
			if node.getParent() == None:
				self.root = node.getLeft()
			else:
				if left==1:
					node.getParent().setLeft(node.getLeft())
				else:
					node.getParent().setRight(node.getLeft())

		else:
			replace = node.getLeft()
			if replace.getLeft()==None and replace.getRight()==None:
				node.setLeft(None)
				node.setVal(replace.getVal())
				return True
			while replace.getRight() != None:
				replace = replace.getRight()

			node.setVal(replace.getVal())
			if replace.getLeft() != None:
				replace.getParent().setRight(replace.getLeft())
			else:
				replace.getParent().setRight(None)

		return True

def main():
	#s = input("Enter a list of numbers: ")
	s = "3 4 2 2.5 2.75 2.74 1 6 903 23 54"
	lst = s.split()

	tree = AVLTree()

	for x in lst:
		tree.insert(float(x))

#	for x in tree:
#		print(x)

	tree.root.trace()
	while True:
		s = input("Enter a number to add: ")
		tree.insert(s)
		tree.root.trace()

if __name__ == "__main__":
	main()

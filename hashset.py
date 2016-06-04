import copy

class HashSet:
	def __init__(self, contents=[]):
		self.items = [None]*10
		self.numItems = 0

		for item in contents:
			self.add(item)

	@staticmethod
	def __add(item,items):
		idx = hash(item)%len(items)
		loc = -1

		while items[idx] != None:
			if items[idx] == item:
				return False

			if loc<0 and type(items[idx]) == HashSet.__Placeholder:
				#Replace the placeholder with item
				loc = idx

			idx = (idx+1)%len(items)

		if loc<0:
			#if found None
			loc = idx

		items[loc] = item

		return True

	@staticmethod
	def __rehash(oldList,newList):
		for x in oldList:
			if x!=None and type(x) != HashSet.__Placeholder:
				HashSet.__add(x,newList)

		return newList

	def add(self,item):
		if HashSet.__add(item,self.items):
			self.numItems += 1
			load = self.numItems/len(self.items)
			if load >= 0.75:
				self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))
	
	class __Placeholder:
		def __init__(self):
			pass

		def __eq__(self,other):
			return False

	@staticmethod
	def __remove(item,items):
		idx = hash(item)%len(items)

		while items[idx] != None:
			if items[idx] == item:
				nextIdx = (idx+1)%len(items)
				if items[nextIdx] == None:
					items[idx] = None
				else:
					items[idx] = HashSet.__Placeholder()
				return True

			print(items[idx])
			idx = (idx+1)%len(items)

		return False

	def remove(self,item):
		if HashSet.__remove(item,self.items):
			self.numItems -= 1
			load = max(self.numItems,10)/len(self.items)
			if load <= 0.25:
				self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
		else:
			raise KeyError("Item not in HashSet")

	def __contains__(self,item):
		idx = hash(item)%len(self.items)
		while self.items[idx]!=None:
			if self.items[idx]==item:
				return True

			idx = (idx+1)%len(self.items)

		return False

	def __iter__(self):
		for i in range(len(self.items)):
			if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
				yield self.items[i]

	def difference_update(self,other):
		for item in other:
			self.discard(item)

	def difference(self,other):
		result = HashSet(self)
		result.difference_update(other)
		return result

	def __getitem__(self,item):
		idx = hash(item)%len(self.items)
		while self.items[idx] != None:
			if self.items[idx] == item:
				return self.items[idx]

			idx = (idx+1)%len(self.items)

		return None	
	
	def __len__(self):
		return self.numItems
		
	def isdisjoint(self,other):
		for item in other:
			if item in self:
				return False

		return True
	
	def issubset(self,other):
		for item in self:
			if item not in other:
				return False

		return True

	def issuperset(self,other):
		for item in other:
			if item not in self:
				return False

		return True
	
	#Make a shallow copy. This is not right
	def copy(self):
		new_set = HashSet()
		new_set.numItems = self.numItems
		new_set.items = copy.deepcopy(self.items)
		return new_set
	
	def union(self,other):
		union_set = self.copy()
		for item in other:
			if item not in self:
				union_set.add(item)

		return union_set

	def intersection(self,other):
		interset = HashSet()
		for item in other:
			if item in self:
				interset.add(item)

		return interset

def main():
	h = HashSet()
	h.add(5)
	h.add(4)
	h.add(123)
	print("length "+str(len(h)))
	h2 = h.copy()
	h2.remove(5)
	print(type(h)==HashSet)
	for i in h2:
		print(i)

if __name__=="__main__":
	main()

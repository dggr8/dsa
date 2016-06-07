import stack as s
import copy

class Position:
	"""
	A class to express position in a cartesian plane
	"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def __eq__(self,other):
		if self.x==other.x and self.y==other.y:
			return True
		else:
			return False
	
	def getNext(self,x,y):
		new_pos = copy.deepcopy(self)
		new_pos.x = self.x + x
		new_pos.y = self.y + y
		return new_pos

def possible_moves(current_position,visited,size):
	all_combinations = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
	all_moves = []
	for comb in all_combinations:
		all_moves.append(current_position.getNext(comb[0],comb[1]))

	temp_stack = s.Stack()
	for move in all_moves:
		if move.getX()<size and move.getX()>=0:
			if move.getY()<size and move.getY()>=0:
				temp_stack.push(move)
	
	moves_stack = s.Stack()
	while not temp_stack.isEmpty():
		move = temp_stack.pop()
		if move not in visited:
			moves_stack.push(move)

	return moves_stack

def print_stack(visited_stack):
	print "Success!!!"
	print "Solution - "
	path_stack = s.Stack()
	while not visited_stack.isEmpty():
		path_stack.push(visited_stack.pop())
	
	while not path_stack.isEmpty():
		pos = path_stack.pop()
		print "%d , %d" %(pos.getX(),pos.getY())
	
def solve_cknight(size,starting_position=[0,0]):
	zero_position = Position(starting_position[0],starting_position[1])

	visited_stack = s.Stack()
	possibility_stacks = s.Stack()
	current_position = zero_position
	stack_count = 0
	visited_stack.push(current_position)
	possibility_stacks.push(possible_moves(current_position,visited_stack,size))

	while len(visited_stack)!=(size*size):

		while not possibility_stacks.top().isEmpty():
			current_position = possibility_stacks.top().pop()
			visited_stack.push(current_position)
			if len(visited_stack) == size*size:
				print_stack(visited_stack)
				return True
			stack_count += 1
			possibility_stacks.push(possible_moves(current_position,visited_stack,size))
			stack_count += 1
			print "A visited stack length %d"%len(visited_stack)

		while possibility_stacks.top().isEmpty():
			possibility_stacks.pop()
			stack_count += 1
			visited_stack.pop()
			stack_count += 1
			print "B visited stack length %d"%len(visited_stack)

		print "stack count = %d" %stack_count
		if visited_stack.isEmpty():
			print "Failure! Couldn't find a solution."
			return False

	print_stack(visited_stack)
	return True

def main():
	solve_cknight(7)

if __name__=="__main__":
	main()

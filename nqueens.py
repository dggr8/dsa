import copy

def clean_allowed(allowed,row_num):
	for row in allowed:
		for j,row_j in enumerate(row):
			if row_j>row_num:
				row[j] = 0

def allowed_update(allowed,row_num,position):
	"""Updates allowed matrix on selection of a
	position"""
	
	size = len(allowed)
	allowed[row_num][position] = row_num+1
	for i in range(row_num+1,size):
		
		j = i-row_num
		#vertical update
		if allowed[i][position] == 0:
			allowed[i][position] = row_num+1
		#left diagonal update
		if position-j >= 0:
			if allowed[i][position-j] == 0:
				allowed[i][position-j] = row_num+1
		#right diagonal update
		if position+j < size:
			if allowed[i][position+j] == 0:
				allowed[i][position+j] = row_num+1


def recur_nq(allowed,row_num,solution):
	"""The recursive function to traverse the board"""
	
	size = len(allowed)
	current_row = allowed[row_num]
	for i in range(size):
		if current_row[i]==0:
			solution[row_num] = i
			if row_num == size-1:
				return True
			allowed_update(allowed,row_num,i)
			recur_nq(allowed,row_num+1,solution)
			if sum(solution)==size*(size-1)/2:
				return True
			else:
				#clean up as we're backtracking
				clean_allowed(allowed,row_num)
				solution[row_num:] = [0]*(size-row_num)
	
	return False

def solve_nq(size):
	""" THE METHOD **goggles emoji** """
	
	a_row = [0]*size
	allowed = []
	for _ in range(size):
		allowed.append(copy.deepcopy(a_row))
	
	solution = [0]*size
	found = recur_nq(allowed,0,solution)
	print "Solution found? ",("yes" if found else "no")
	for row in allowed:
		print row
	print "----------------------------"
	print [[i+1,j+1] for i,j in enumerate(solution)]

def main():
	solve_nq(8)

if __name__=="__main__":
	main()

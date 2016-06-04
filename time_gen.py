i = 0 #hour counter
j = 0 #min counter
for i in range(0,24):
	for j in range(0,60,10):
		next_i = i
		next_j = j + 10
		if next_j == 60:
			next_i = (next_i+1)%24
			next_j = 0
		if i<10:
			one = "0"+str(i)
		else:
			one = str(i)
		if j==0:
			two = "00"
		else:
			two = str(j)
		if next_i < 10:
			three = "0"+str(next_i)
		else:
			three = str(next_i)
		if next_j==0:
			four = "00"
		else:
			four = str(next_j)
		
		print(one+":"+two+" to "+three+":"+four)

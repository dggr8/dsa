import random

def partition(seq,start,stop):

	pivotIndex = start
	pivot = seq[pivotIndex]
	i = start+1
	j = stop-1

	while i<=j:
		while i<=j and not pivot < seq[i]:
			i+=1
		while i<=j and pivot < seq[j]:
			j-=1

		if i < j:
			seq[i],seq[j] = seq[j],seq[i]
			i+=1
			j-=1

	seq[pivotIndex] = seq[j]
	seq[j] = pivot

	return j

def quicksortRecursively(seq,start,stop):
	if start >= stop-1:
		return

	pivotIndex = partition(seq,start,stop)

	quicksortRecursively(seq,start,pivotIndex)
	quicksortRecursively(seq,pivotIndex+1,stop)

def quicksort(seq):
	#randomize the sequence first
	for i in range(len(seq)):
		j = random.randint(0,len(seq)-1)
		seq[i],seq[j] = seq[j],seq[i]
	
	quicksortRecursively(seq,0,len(seq))	


list = [3,4,2,5,1,6,8,12,7]
quicksort(list)
print(list)

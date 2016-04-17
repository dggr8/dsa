import datetime
import random
import time

def main():

	# Write an XML file with the results
	file = open("ListAccessTiming.xml","w")

	file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

	file.write('<Plot title="Average List Element Access Time">\n')

	# Test lists of size 1000 to 200000.
	xmin = 1000
	xmax = 200000

	# Record the list sizes in xList and average access time
	xList = []
	yList = []

	for x in range(xmin, xmax+1, 1000):

		xList.append(x)

		prod = 0

		# Creates a list of size x with all 0's 
		lst = [0]*x

		# settle down
		time.sleep(1)

		#Time before the 1000 test retrievals
		starttime = datetime.datetime.now()

		for v in range(1000):
			# Find a random location and retrieve
			index = random.randint(0,x-1)
			val = lst[index]
			prod = prod*val

		#Time after 1000 test retrievals
		endtime = datetime.datetime.now()

		# The difference in the time between start and end
		deltaT = endtime - starttime

		# divide by 1000 and multiply by 10^6 for microseconds
		accessTime = deltaT.total_seconds()*1000

		yList.append(accessTime)

	file.write('  <Axes>\n')
	file.write('     <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">List Size</XAxis>\n')
	file.write('     <YAxis min="'+str(min(yList))+'" max="'+str(60)+'">Microseconds</YAxis>\n')
	file.write('  </Axes>\n')

	file.write('  <Sequence title="Average Access Time vs List Size" color="red">\n')

	for i in range(len(xList)):
		file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

	file.write('  </Sequence>\n')

	# This program tests access at 100 random locations of a 200000 elements
	xList = lst
	yList = [0]*200000

	time.sleep(2)

	for i in range(100):
		starttime = datetime.datetime.now()
		index = random.randint(0,200000-1)
		xList[index] = xList[index]+1
		endtime = datetime.datetime.now()
		deltaT = endtime - starttime
		yList[index] = yList[index] + deltaT.total_seconds() *1000000

	file.write('   <Sequence title="Access Time Distribution" color="blue">\n')

	for i in range(len(xList)):
		if xList[i] > 0:
			file.write('     <DataPoint x="'+str(i)+'" y="'+str(yList[i])+'"/>\n')

	file.write('   </Sequence>\n')
	file.write('</Plot>\n')
	file.close()

if __name__ == '__main__':
	main()
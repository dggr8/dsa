
f = open('routes.txt','r')

routes = []
for line in f:
	routes.append([int(k) for k in line.split()])

number_of_drivers = len(routes)
n = number_of_drivers
# n is the number_of_drivers and number_of_gossips

gossip = [[0]*n for i in range(n)]
for i in range(n):
	gossip[i][i] = 1

gossip_done = 0
len_routes = [len(k) for k in routes]
max_iter = 1
for i in len_routes:
	max_iter *= i
num_iter = 0

while gossip_done==0:
	if num_iter==max_iter-1:
		break

	#update secrets
	for i in range(n):
		j = i
		len_route_i = len(routes[i])
		while j <= n-1:
			len_route_j = len(routes[j])
			if routes[i][num_iter%len_route_i] == routes[j][num_iter%len_route_j]:
				# resulting gossip array for the two drivers is the bitwise OR of the two arrays
				gossip[i] = [gossip[i][k]|gossip[j][k] for k in range(n)]
				gossip[j] = [gossip[i][k]|gossip[j][k] for k in range(n)]
		
			j+=1

	#check if gossip is done
	total_gossip = 0
	for driver in gossip:
		total_gossip += sum(driver)

	if total_gossip==n*n:
		#n*n is the max gossip possible
		gossip_done = 1
	num_iter+=1

if gossip_done==1:
	print(num_iter)
else:
	print("never")
	
f.close()
def recursive_fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return recursive_fibo(n-1)+recursive_fibo(n-2)

memo = {}
def memo_fibo(n):
	if n in memo:
		return memo[n]

	if n==0:
		memo[0] = 0
		return 0

	if n==1:
		memo[1] = 1
		return 1

	val = memo_fibo(n-1)+memo_fibo(n-2)
	memo[n] = val

	return val

def main():
	print(memo_fibo(75))

if __name__ == "__main__":
	main()

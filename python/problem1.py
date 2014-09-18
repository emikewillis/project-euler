def problem1(n):
	return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])

print(problem1(10))
print(problem1(1000))

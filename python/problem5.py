def div_by(b,f):
	return True if b % f == 0 else False

def div_by_range(n,start,end):
	for x in range(start,end+1):
		if not div_by(n,x):
			return False

	return True

# This sure does take a while
def find_product_of_range(start,end):
	n = end
	while not div_by_range(n,start,end):
		n += end

	return n

print(find_product_of_range(1,10))
print(find_product_of_range(1,20))

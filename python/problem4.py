def is_palindrome(astr):
	return astr == astr[::-1]


def all_possible_products_between(start,end):
	products = []
	
	for a in range(start,end+1):
		for b in range(a,end+1):
			products.append(a*b)

	return products

def all_palindromes_between(start,end):
	# Is there a convention for nested function calls like this that makes it more readable?
	# or should I be using temp vars to hold each succesive step?
	return filter((lambda a: is_palindrome(str(a))),
	               all_possible_products_between(start,end))

def largest_palindrome(start,end):
	return max(all_palindromes_between(start,end))

print(largest_palindrome(10,99))
print(largest_palindrome(100,999))

import math
from functools import partial

def divisible_by(b,f):
	return True if b % f == 0 else False

def prime_factors(n):
	factors = []
	
	s = 2
	a = n
	while True:
		#[factor (first (filter #(zero? (mod n %))
		#            (range s (inc (int (Math/sqrt n))))))]
		factor = range(s,int((math.sqrt(a)+1)))
		factor = filter(partial(divisible_by,a),factor)
		factor = factor[0] if factor != [] else None

		if factor == None:
			factors.append(a)
			break

		a = a / factor
		s = factor
		factors.append(factor)
	
	return factors

print(prime_factors(13195))
print(max(prime_factors(600851475143)))

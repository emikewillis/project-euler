def fib(mx):
	a,b = 0,1
	while a < mx:
		yield a
		a,b = b,a+b

fibnums = fib(4000000)
a = 0
for i in fibnums:
	if i % 2 == 0:
		#print(i)
		a += i

print(a)

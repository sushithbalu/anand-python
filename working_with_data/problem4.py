def my_product(x):
	p = 1
	for v in x:
		p *= v
	return p

print my_product([1,10,100])

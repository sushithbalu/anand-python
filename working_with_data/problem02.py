def my_sum(x):
	s = 0
	for v in x:
		s += v
	return s

print my_sum([1,2,4,5,6])
print my_sum([1])
print my_sum(["apple","orange", "mango"])

def fact(x):
	s = 1
	if x < 2:
		return 1 #factorial of zero = one
	else:
		for v in range(x,1):
			s = s + v*(v-1)
		return s

print fact(4)

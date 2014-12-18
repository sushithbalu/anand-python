def my_max(x):
	s = 0
	for v in x:
		for a in range(len(x)):
			if v < x[a]:
				s = x[a]
	return s
print my_max(["ew", "rfger", "efe"])

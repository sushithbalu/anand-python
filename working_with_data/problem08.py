def cum_sum(x):
	s = 0
	l = []
	for v in x:
		s += v
		l.append(s)
	return l

x = [1,2,3,4,6,8]
print "x =", x,"\ncumulative sum of x = ", cum_sum(x)
		 

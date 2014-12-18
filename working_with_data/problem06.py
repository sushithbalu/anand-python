def reverse(x):
	if type(x) == list:
		y = []
		for v in range(1, len(x)+1):
			y.append(x[-v])
		return y
	else:
		print "not a list"
		return 0

x = 12 
print "\nx =", x
print "reverse(x) =", reverse(x)
print "reverse(reverse(x)) =", reverse(reverse(x)),"\n"

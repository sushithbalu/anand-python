x = 1
def f():
	global x #global x
	y =  x 
	x = 2 #global x redefined
	return x + y
print x
print f()
print x

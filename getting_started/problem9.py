#global
x = 1
def f():
	#local
	x = 2
	return x
print x
print f()
print x

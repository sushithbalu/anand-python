numcalls = 0
def square(x):
	global numcalls
	numcalls = numcalls + 1
	return x*x

print square(5)
print square(2+5)
#python fuctions are not like #define in c.
#square(2+5); square(7); 49

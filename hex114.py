import sys
i=0
def fac(n):
	global i
	if n == 0:	
		return 1
	else:
		i+=1
		return n*fac(n-1)
	
fac(int(input()))
print(i)


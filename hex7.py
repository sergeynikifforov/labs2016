import matplotlib.pyplot as plt
import numpy as np
a=int(input())
b=float(input())
if (a%2==0) or (b>=1) or (a==1) or (b<=0):
	print('error')
else:
	x = np.arange(0, 10,0.01)
	q=0
	for i in range(0,100):
		q=q+b**i*np.cos(a**i*np.pi*x)
	plt.plot(x,q)
	plt.grid(True)
	plt.show()


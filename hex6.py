import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
t = np.arange(0.99, 5, 0.01)
p = np.polyfit(x, y, deg=3)
p1 = np.polyfit(x, y, deg=1)
p2 = np.polyfit(x, y, deg=2)
for i in range (0,5):
	plt.errorbar(x[i], y[i], xerr=(0.000003*(x[i])**2+x[i]*0.05), yerr=y[i]*0.04)
plt.errorbar(x, y)
p_f = np.poly1d(p)
plt.plot(t,p_f(t))
p_f = np.poly1d(p1)
plt.plot(t,p_f(t))
p_f = np.poly1d(p2)
plt.plot(t,p_f(t))
plt.grid()
plt.show()


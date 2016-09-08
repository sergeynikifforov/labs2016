import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-100, 100.01, 1)
plt.plot(x,np.log((x**2+1),1+np.tan(1/(1+(np.sin(x))**2)))*np.e**(-abs(x)/10))
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 3.01, 0.01)
plt.plot(x,x*x-x-6)
plt.grid(True)
plt.show()

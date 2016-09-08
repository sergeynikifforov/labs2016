import numpy as np
import pylab
from matplotlib import mlab
t = np.arange(0, 2*np.pi, 0.01)
pylab.ion()
pylab.xkcd()
a = 1
while a<100:
    pylab.clf()
    pylab.plot (np.sin(t+a),np.cos(2*t))
    pylab.draw()
    a+=1

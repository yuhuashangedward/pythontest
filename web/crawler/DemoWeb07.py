import numpy as np
import matplotlib.pyplot as plt
t= np.arange(0,10)

plt.plot(t, t+2)
plt.plot(t,t,'O',t,t+2,t,t**2,'O')
plt.bar(t,t**2)

plt.show()

import pylab as pl
t=np.arange(0,10)

plt.plot(t,t+2)
plt.show()
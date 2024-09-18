import numpy as np
import matplotlib.pyplot as plt

x = np.array([4,7,8,5,2])
y = np.array([1,3,5,7,9])

plt.subplot(1,2,1)
plt.plot(x,y)

x = np.array([1,3,5,7,9])
y = np.array([4,7,8,5,2])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()

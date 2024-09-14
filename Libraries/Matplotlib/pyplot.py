#   what is pyplot ?
'''  
The name pyplot is a combination of two words:

1.  py: This stands for Python.
2.  plot: This refers to the action of creating a plot or chart, which is a graphical representation of data. 
'''

#   why pyplot ?
'''
pyplot essentially means "Python plotting." It is a module in Matplotlib that provides a set of functions
for creating and customizing various types of plots (like line charts, bar charts, scatter plots, etc.)
in a simple and straightforward way. The name reflects its purpose: making plotting easy in Python.
'''

# without using Numpy :

import matplotlib.pyplot as plt

x = [1,10]
y = [3,8]

plt.plot(x,y)
plt.show()


# with using Numpy :

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,10])
y = np.array([3,8])

plt.plot(x,y)
plt.show()

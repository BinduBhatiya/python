import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.title('display data')
plt.xlabel('x label')
plt.ylabel('y label')

#plt.grid(axis='y')      # if we can pass axis='x' then it will return axis line horizontaly.
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
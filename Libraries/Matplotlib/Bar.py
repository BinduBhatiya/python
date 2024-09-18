import numpy as np
import matplotlib.pyplot as plt

# x = np.array(['A','B','C','D'])
# y = np.array([4,5,3,7])

x = ['apple','banana']  # we can use this type of pattern.
y = [10,20]             # same

# plt.bar(x,y)
# plt.barh(x,y)         # it is used for set pipe as horizontally.
plt.bar(x,y,color='green', width=0.5)

plt.show()
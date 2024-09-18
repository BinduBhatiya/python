import numpy as np
import matplotlib.pyplot as plt

y = np.array([20,10,50,15,5])
mylabel = ['apple','banana','cherry','grapes','orange']
myexplode = [0.2, 0, 0, 0, 0]

plt.pie(y, labels=mylabel, explode=myexplode, shadow=True)
plt.legend()

plt.show()
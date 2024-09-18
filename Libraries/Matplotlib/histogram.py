import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(170,10,120)    # (mean, standard_deviation, size)

plt.hist(x)     # create histogram

plt.show()
# Normal Distribution.
'''
The Normal Distribution is one of the most important distributions.
It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
Use the random.normal() method to get a Normal Data Distribution.
It has three parameters:
    loc - (Mean) where the peak of the bell exists.
    scale - (Standard Deviation) how flat the graph distribution should be.
    size - The shape of the returned array.
'''

# normal distribution with simple size argument.
from numpy import random
arr = random.normal(size=(2,3))
print("normal distribution: ",arr)


# output :
'''
normal distribution:  [[-1.02197497 -1.22456284 -0.21758633]
                       [ 0.29012379  0.41487473 -0.42380576]]
'''

# normal distribution with mean(loc) and standard deviation(scale) and size(row, column) argument
from numpy import random
arr = random.normal(loc=10, scale=20, size=(2,3))
print("using mean and standard deviation mode: ",arr)

# output :
'''
using mean and standard deviation mode:  [[  1.69889091  12.95062311 -31.50291513]
                                          [ -9.09555791  28.74405666  13.03981765]]
'''


# normal distribution using matplotlib.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=10), hist=False)
plt.show()

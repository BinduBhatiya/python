# logistic distribution.

from numpy import random
arr = random.logistic(loc=10, scale=20, size=(2,3))
print("using mean and standard deviation mode: ",arr)

# output :
'''
using mean and standard deviation mode:  [[  1.69889091  12.95062311 -31.50291513]
                                          [ -9.09555791  28.74405666  13.03981765]]
'''


# visulisation.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=10), hist=False)
sns.distplot(random.normal(size=10), hist=False)
plt.show()
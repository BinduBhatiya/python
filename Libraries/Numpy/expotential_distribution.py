# expotential distribution
# it is used to describe the time till next element that is like failur or success.
# parameter: (scale), (size)

# simple expotential distribtion
from numpy import random
arr = random.exponential(scale=5, size=(2,3))
print("simple expotential value: ",arr)

# output :
'''
simple expotential value:  [[ 1.11246358  3.6052142  16.21646731]
                            [ 1.56620574 22.74808018  2.95317633]]
'''


# visulization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=(10)),hist=True)
plt.show()
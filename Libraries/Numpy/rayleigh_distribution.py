# rayleigh distribution is used in single processing.
# parameter :
# scale(how flate the distribution is ... default 1.0), size

# simple rayleigh distribtion
from numpy import random
arr = random.rayleigh(scale=5, size=(2,3))
print("simple rayleigh value: ",arr)

# output :
'''
simple rayleigh value:  [[4.1664163  3.6275884  5.64762882]
                          [ 5.86922028 8.00471675 6.0923341 ]]
'''



# visulization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(scale=5,size=(10)),hist=True)
plt.show()
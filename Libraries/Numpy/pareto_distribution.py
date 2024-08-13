# pareto distribution :
# parameter :
# a(shape) , size

# simple chi square distribtion
from numpy import random
arr = random.pareto(a=5, size=(2,3))
print("simple pareto value: ",arr)

# output :
'''
simple pareto value:  [[0.2319274  0.67186836 0.04863834]
                       [0.27672889 0.00500666 0.17173164]]
'''



# visulization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=5,size=(1000)),hist=True,kde=False)
plt.show()
# uniform distribution.
# it has three parameter. a=lower bound(0.0) , b=upper bound(1.0) , size(shape of array)

# simple use of uniform distribution.
from numpy import random
arr = random.uniform(size=(2,3))
print("uniform distribution is: ",arr)

# output :
'''
uniform distribution is:  [[0.95995259 0.65758716 0.93704032]
                           [0.21488444 0.14611287 0.98712093]]
'''


# visulization of uniform distribution.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=10),hist=False,kde=True)
plt.show()
# binomial distribution - descrete distribution - binary output
''' 
argument :
                n(number of trials) 
                p(Probability)
                size(number of size)
'''

# using simple binomial argument.
from numpy import random
arr = random.binomial(n=10, p=0.5, size=10)
print("simple binomial data: ",arr)

# output :
# simple binomial data:  [6 3 8 5 4 7 4 5 6 7]


# print data in diagram.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000),hist=True,kde=True)
plt.show()
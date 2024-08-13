# poisson distribution :
# the poisson distribution is used to generate random number. which all random array values "sum" is devided by "size value" and after become "division == lam".
# in simple word,here lam is similar to average or mean.


# using simple poisson distribution.
from numpy import random
arr = random.poisson(lam=5, size=10)
print("simple poission distribution: ",arr)


# visualization :
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=5, size=10),hist=True,kde=False)
plt.show()


# difference between binomial distribution and poisson distribution.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=10),hist=False,kde=True,label='binomial')
sns.distplot(random.poisson(lam=2, size=10),hist=False,kde=True,label='poisson')
plt.show()
# simple chi square distribtion
from numpy import random
arr = random.chisquare(df=5, size=(2,3))
print("simple chisquare value: ",arr)

# output :
'''
simple chisquare value:  [[ 4.89100054  3.46817634  2.91608551]
                          [ 6.22598394 11.4709416   4.52964431]]
'''



# visulization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=5,size=(10)),hist=True)
plt.show()
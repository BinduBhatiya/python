# zipf : its defination is like common word in english has occurs and nearly 1/5 time as of the most hindi words. 
# prameter :
# a() : distribution parameter
# size

# simple chi square distribtion
from numpy import random
arr = random.zipf(a=2, size=(2,3))
print("simple zipf value: ",arr)

# output :
'''
simple zipf value:   [[ 1 10  1]
                      [ 1  2  1]]
'''



# visulization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.zipf(a=2, size=(1000))
sns.distplot(arr[arr<10],hist=True,kde=False)
plt.show()
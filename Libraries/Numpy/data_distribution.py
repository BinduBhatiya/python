# what is Data Distribution ?
'''
Data Distribution is a list of all possible values, and how often each value occurs.
Such lists are important when working with statistics and data science.
The random module offer methods that returns randomly generated data distributions.
'''

from numpy import random
x = random.choice([1,3,5,7], p=[0.0,0.2,0.2,0.6], size=(50))
print(x)

# output :
'''
[7 7 5 7 7 5 7 5 7 7 7 7 7 5 7 5 7 7 7 7 3 7 7 7 7 5 7 5 5 7 5 7 7 7 7 7 5
 7 5 5 3 7 7 7 7 5 7 7 7 5]
'''
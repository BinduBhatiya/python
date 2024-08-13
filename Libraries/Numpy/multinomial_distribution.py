# multinomial distribution
# multinomial sample will not produce a single value. they will produce one value for each pvals.
# draw out a sample for dice roll.

from numpy import random
arr = random.multinomial(n=10, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(2,4))
print("multinomial distribution: ",arr)

# output :
'''
[[[1 2 3 1 1 2][2 0 3 3 2 0][0 2 2 4 2 0][0 3 2 4 1 0]]
  [[2 0 1 3 1 3][3 0 1 3 3 0][1 1 0 4 3 1][0 0 2 5 1 2]]]
'''

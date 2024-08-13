# generate random number.

from numpy import random
x = random.randint(5)
print(x)        # generate random number from 0 to 5. 


# generate random float.

from numpy import random 
x = random.rand()
print(x)        # generate random number from 0 to 1.


# generate random array.

from numpy import random 
x = random.randint(100, size=5)
print(x)            # [29 58 46  6 49] generate any 5 value from 0 to 100


# generate 2D array.

from numpy import random 
x = random.randint(10, size=(3,5))
print(x)

# output :
'''
[[2 0 3 8 3]
 [0 7 8 7 3]
 [3 0 6 9 8]]
'''


from numpy import random 
x = random.randint(5, size=(3,5))   # generate 2D array and print value between 0 to 5.
print(x)

# output :
'''
[[4 0 4 3 0]
 [3 1 1 4 2]
 [4 3 2 1 3]]
'''


# generate random number from array.
from numpy import random
x = random.choice([1,5,9,3], size=(2,2))    # it print random value from given array.
print(x)

# output :
'''
[[1 5]
 [9 1]]
'''

# FIND THE MAXIMUM VALUE FROM TWO VALUE.

from functools import reduce

num = [10,20]

res = reduce(lambda x,y: x if x > y else y, num)
print("maximum is: ",res)                                       # maximum is:  20
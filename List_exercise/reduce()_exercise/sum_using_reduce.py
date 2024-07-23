# SUM OF 5 NUMBER :

from functools import reduce
number = [1,2,3,4,5]
res = reduce(lambda x,y: x + y , number)
print("sum is: ",res)                                                  # sum is:  15
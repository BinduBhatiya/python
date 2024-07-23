# FIND THE FACTORIAL VALUE

from functools import reduce

n = 5
fact = reduce(lambda x,y: x * y, range(1, n+1))
print("factorial is: ",fact)                                        



# factorial is:  120
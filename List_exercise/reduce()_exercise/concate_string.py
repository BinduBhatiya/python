# CONCATE STRING USING REDUCE.

from functools import reduce

lst = ['hello', 'python', 'world']
res = reduce(lambda x,y:  x +' '+y , lst)
print(res)                                              # hello python world

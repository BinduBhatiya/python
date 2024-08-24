# PRINT TUPLE VALUE MUTIPLE TIME

tup = (1,3)
n = 4
res = (tup,) * n
print(tuple(res))               # ((1, 3), (1, 3), (1, 3), (1, 3))
res = (tup) * n
print(tuple(res))               # (1, 3, 1, 3, 1, 3, 1, 3)
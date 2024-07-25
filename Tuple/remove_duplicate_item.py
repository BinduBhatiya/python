# HOW TO REMOVE DUPLICATE ITEM IN TUPLE.

tup = (1,3,9,2,3,5,2,8,3)
res = set(tup)
print(tuple(res))                   # (1, 2, 3, 5, 8, 9)


# USING FOR LOOP
tup = (1,3,9,2,3,5,2,8,3)
lst = []

for i in tup:
    if i not in lst:
        lst.append(i)
print(tuple(lst))                   # (1, 3, 9, 2, 5, 8)
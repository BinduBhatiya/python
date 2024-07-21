# INTERSECTION OF TWO NESTED LIST

lst1 = [[1,2],[3,4],[5,6]]
lst2 = [[6,7],[1,2],[8,9]]

print('list 1 is: ',lst1)
print('list 2 is: ',lst2)

res = [i for i in lst1 if i in lst2]
print(res)

# OUTPUT :
'''
list 1 is:  [[1, 2], [3, 4], [5, 6]]
list 2 is:  [[6, 7], [1, 2], [8, 9]]
[[1, 2]]
'''


# INTERSECTION OF TWO NESTED LIST DEFINE IN BOOLEAN VALUE IS IT TRUE OR FALSE

lst1 = [[1,2],[3,4],[5,6]]
lst2 = [[6,7],[1,2],[8,9]]

print('list 1 is: ',lst1)
print('list 2 is: ',lst2)

res = [i for i in lst1 if i in lst2]
print(bool(res))

# OUTPUT :
'''
list 1 is:  [[1, 2], [3, 4], [5, 6]]
list 2 is:  [[6, 7], [1, 2], [8, 9]]
True
'''


# CHECK NESTED LIST IS SUBSET OF ANOTHER NESTED LIST

def check_subset(lst1, lst2):
    l1,l2 = lst1[0],lst2[0]
    exist = True

    for i in lst2:
        if i not in lst1:
            exist = False
    return exist

lst1 = [[1,2],[3,4],[5,6]]
lst2 = [[6,7],[1,2],[8,9]]                  # if lst2 = [[1,2], [3,4]] then it will return "True".
print(check_subset(lst1, lst2))


# OUTPUT :
# False




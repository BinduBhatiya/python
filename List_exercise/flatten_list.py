# FLATTEN A LIST OF LIST

lst = [[1,3,"geeks"], [4,5], [6,"best"]]
res = [i for row in lst for i in row]
print(res)


# OUTPUT :
'''
[1, 3, 'geeks', 4, 5, 6, 'best']
'''

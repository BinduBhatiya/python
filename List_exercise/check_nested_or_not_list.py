# CHECK THE LIST IS NESTED OR NOT

lst = [[8,2,3],[4,5],[6],[7,8]]
res = False
for i in lst:
    if type(i) == list:
        res = True
        break
print('is list is nested ? ',bool(res))